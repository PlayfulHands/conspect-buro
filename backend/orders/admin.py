from django.contrib import admin
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from .models import Order
from import_export.admin import ExportActionMixin


@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    # Колонки в списке заявок
    list_display = [
        'id',
        'created_at_formatted',
        'client_info',
        'order_details',
        'estimated_price_display',
        'deadline_status',
        'status_badge',
        'admin_actions',
    ]

    # По каким полям можно искать
    search_fields = ['vk_link', 'phone', 'additional_info']

    # Фильтры справа
    list_filter = [
        'is_processed',
        'paper_format',
        'handwriting',
        'get_type',
        'has_material',
        ('deadline', admin.DateFieldListFilter),
        ('created_at', admin.DateFieldListFilter),
    ]

    # Кликабельные поля
    list_display_links = ['id', 'client_info']

    # Поля только для чтения
    readonly_fields = ['created_at', 'estimated_price']

    # Группировка полей при редактировании заявки
    fieldsets = [
        ('📋 Информация о заявке', {
            'fields': [
                'is_processed',
            ]
        }),
        ('👤 Контакты клиента', {
            'fields': [
                'vk_link',
                'phone',
            ]
        }),
        ('📝 Параметры работы', {
            'fields': [
                'pages',
                'deadline',
                'paper_format',
                'handwriting',
                'has_material',
            ]
        }),
        ('🎨 Дополнительно', {
            'fields': [
                'has_tables',
                'has_schemes',
                'has_drawings',
                'text_only',
                'additional_info',
            ]
        }),
        ('🚚 Доставка', {
            'fields': [
                'get_type',
            ]
        }),
        ('💰 Финансы', {
            'fields': [
                'estimated_price',
            ]
        }),
    ]

    # Действия с заявками
    actions = ['mark_as_processed', 'mark_as_unprocessed', 'export_as_csv']

    # Количество заявок на странице
    list_per_page = 50

    # Форматированные поля для отображения

    @admin.display(description='Дата создания', ordering='created_at')
    def created_at_formatted(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')

    @admin.display(description='Клиент')
    def client_info(self, obj):
        vk = obj.vk_link.replace('https://vk.com/', '').replace('https://m.vk.com/', '')
        return format_html(
            '<div style="white-space: nowrap;">'
            '<div style="font-weight: 600; font-size: 14px;">{}</div>'
            '<div style="color: #666; font-size: 12px;">{}</div>'
            '</div>',
            vk,
            obj.phone
        )

    @admin.display(description='Детали заказа')
    def order_details(self, obj):
        extras = []
        if obj.has_tables:
            extras.append('📊')
        if obj.has_schemes:
            extras.append('📐')
        if obj.has_drawings:
            extras.append('🎨')
        if obj.text_only:
            extras.append('📝')

        format_map = {
            'A4_tetrad': 'А4 тет.',
            'A5_tetrad': 'А5 тет.',
            'A4_list': 'А4 лист',
        }

        return format_html(
            '<div style="font-size: 13px;">'
            '<span style="font-weight: 600;">{} стр.</span> · {}<br>'
            '<span style="color: #888;">{}{}</span>'
            '</div>',
            obj.pages,
            format_map.get(obj.paper_format, obj.paper_format),
            ' '.join(extras) + ' ' if extras else '',
            obj.get_handwriting_display()
        )

    @admin.display(description='Цена', ordering='estimated_price')
    def estimated_price_display(self, obj):
        return format_html(
            '<span style="font-weight: 700; font-size: 15px; color: #27ae60;">{} ₽</span>',
            obj.estimated_price
        )

    @admin.display(description='Срок', ordering='deadline')
    def deadline_status(self, obj):
        days_left = (obj.deadline - timezone.now().date()).days

        if days_left < 0:
            color = '#e74c3c'
            bg = '#ffeaea'
            text = f'Просрочено ({abs(days_left)} дн.)'
        elif days_left == 0:
            color = '#e67e22'
            bg = '#fff3e0'
            text = 'Сегодня!'
        elif days_left <= 2:
            color = '#e67e22'
            bg = '#fff3e0'
            text = f'{days_left} дн.'
        else:
            color = '#27ae60'
            bg = '#eafaf1'
            text = f'{days_left} дн.'

        return format_html(
            '<div style="text-align: center; font-size: 12px;">'
            '<span style="display: block; font-size: 11px; color: #888;">{}</span>'
            '<span style="display: inline-block; padding: 2px 8px; border-radius: 10px; '
            'background: {}; color: {}; font-weight: 600;">{}</span>'
            '</div>',
            obj.deadline.strftime('%d.%m.%Y'),
            bg, color, text
        )

    @admin.display(description='Статус', ordering='is_processed')
    def status_badge(self, obj):
        if obj.is_processed:
            return format_html(
                '<span style="display: inline-block; padding: 4px 12px; border-radius: 12px; '
                'background: #d4edda; color: #155724; font-weight: 600; font-size: 12px;">'
                '{} Обработана</span>',
                '✅'
            )
        return format_html(
            '<span style="display: inline-block; padding: 4px 12px; border-radius: 12px; '
            'background: #fff3cd; color: #856404; font-weight: 600; font-size: 12px;">'
            '{} Новая</span>',
            '🆕'
        )

    @admin.display(description='')
    def admin_actions(self, obj):
        if obj.is_processed:
            return format_html(
                '<a href="{}" style="color: #888; text-decoration: none; font-size: 12px;">↩ Вернуть</a>',
                reverse('admin:orders_order_change', args=[obj.id])
            )
        return format_html(
            '<a href="{}" style="color: #27ae60; text-decoration: none; font-weight: 600; font-size: 12px;">✓ Взять в работу</a>',
            reverse('admin:orders_order_change', args=[obj.id])
        )

    # Действия

    @admin.action(description='✅ Отметить как обработанные')
    def mark_as_processed(self, request, queryset):
        updated = queryset.update(is_processed=True)
        self.message_user(request, f'{updated} заявок отмечено как обработанные.')

    @admin.action(description='🔄 Вернуть в новые')
    def mark_as_unprocessed(self, request, queryset):
        updated = queryset.update(is_processed=False)
        self.message_user(request, f'{updated} заявок возвращено в новые.')

    @admin.action(description='📥 Экспортировать в CSV')
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response, delimiter=';')
        writer.writerow([
            'ID', 'Дата', 'ВК', 'Телефон', 'Страниц', 'Дедлайн',
            'Формат', 'Почерк', 'Материал', 'Таблицы', 'Схемы',
            'Рисунки', 'Текст', 'Доп. инфо', 'Получение', 'Цена', 'Статус'
        ])

        for obj in queryset:
            writer.writerow([
                obj.id,
                obj.created_at.strftime('%d.%m.%Y %H:%M'),
                obj.vk_link,
                obj.phone,
                obj.pages,
                obj.deadline.strftime('%d.%m.%Y'),
                obj.get_paper_format_display(),
                obj.get_handwriting_display(),
                obj.get_has_material_display(),
                'Да' if obj.has_tables else '',
                'Да' if obj.has_schemes else '',
                'Да' if obj.has_drawings else '',
                'Да' if obj.text_only else '',
                obj.additional_info,
                obj.get_get_type_display(),
                obj.estimated_price,
                'Обработана' if obj.is_processed else 'Новая',
            ])

        return response


# Настройка заголовков админки
admin.site.site_header = 'Конспект Бюро — Управление заявками'
admin.site.site_title = 'Конспект Бюро'
admin.site.index_title = 'Панель управления заявками'