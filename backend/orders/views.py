import requests
from django.conf import settings
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer


def send_vk_notification(order):
    token = settings.VK_GROUP_TOKEN
    if not token:
        return

    message = (
        f"📥 Новая заявка №{order.id}\n"
        f"👤 ВК: {order.vk_link}\n"
        f"📞 Телефон: {order.phone}\n"
        f"📄 Страниц: {order.pages}\n"
        f"💰 Сумма: {order.estimated_price} ₽"
    )

    try:
        requests.post(
            "https://api.vk.com/method/messages.send",
            data={
                "access_token": token,
                "v": "5.199",
                "peer_id": 236864312,
                "message": message,
                "random_id": 0,
            },
            timeout=5,
        )
    except Exception as e:
        print(f"VK notify error: {e}")


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        order = serializer.save()
        send_vk_notification(order)
        return Response({
            'success': True,
            'message': 'Заявка успешно создана! Мы свяжемся с вами в ближайшее время.',
            'order_id': order.id
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'success': False,
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_client_orders(request):
    """Возвращает список заявок по номеру телефона или ссылке ВК."""
    phone = request.GET.get('phone', '')
    vk = request.GET.get('vk', '')
    
    if not phone and not vk:
        return Response({
            'success': False,
            'error': 'Укажите телефон или ссылку ВК для поиска'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    orders = Order.objects.all()
    
    if phone:
        orders = orders.filter(phone__icontains=phone)
    if vk:
        orders = orders.filter(vk_link__icontains=vk)
    
    orders = orders.order_by('-created_at')
    serializer = OrderSerializer(orders, many=True)
    
    return Response({
        'success': True,
        'orders': serializer.data
    })