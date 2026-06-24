from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'vk_link', 'phone', 'pages', 'deadline', 'estimated_price', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at']
    search_fields = ['vk_link', 'phone']