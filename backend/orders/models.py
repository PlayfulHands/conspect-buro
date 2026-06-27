from django.db import models

class Order(models.Model):
    WORK_TYPE_CHOICES = [
        ('conspect', 'Конспект'),
    ]
    
    FORMAT_CHOICES = [
        ('A4_tetrad', 'Тетрадь А4'),
        ('A5_tetrad', 'Тетрадь А5'),
    ]
    
    HANDWRITING_CHOICES = [
        ('any', 'Стандарт'),
        ('readable', 'Разборчивый'),
        ('individual', 'Индивидуальный подбор'),
    ]
    
    MATERIAL_TYPE_CHOICES = [
        ('document', 'Электронный документ'),
        ('presentation', 'Презентация'),
        ('handwritten_photo', 'Фото рукописного конспекта'),
    ]

    # Контакты
    vk_link = models.URLField(verbose_name="Ссылка ВКонтакте")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    delivery_address = models.CharField(max_length=500, verbose_name="Адрес ПВЗ Wildberries", default='')
    
    # Параметры работы
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, default='conspect')
    material_type = models.CharField(max_length=30, choices=MATERIAL_TYPE_CHOICES, default='document', verbose_name="Тип материала")
    pages = models.PositiveIntegerField(verbose_name="Объем работы (стр.)")
    deadline = models.DateField(verbose_name="Срок сдачи")
    paper_format = models.CharField(max_length=20, choices=FORMAT_CHOICES, verbose_name="Формат")
    handwriting = models.CharField(max_length=20, choices=HANDWRITING_CHOICES, verbose_name="Почерк")
    
    # Дополнительно
    has_tables = models.BooleanField(default=False, verbose_name="Таблицы")
    has_schemes = models.BooleanField(default=False, verbose_name="Схемы")
    has_drawings = models.BooleanField(default=False, verbose_name="Рисунки")
    text_only = models.BooleanField(default=False, verbose_name="Только текст")
    additional_info = models.TextField(blank=True, verbose_name="Дополнительная информация")
    
    # Доставка
    get_type = models.CharField(max_length=20, default='delivery', verbose_name="Способ получения")
    
    # Файлы
    uploaded_file = models.FileField(upload_to='orders/%Y/%m/', verbose_name="Файл с материалом", blank=True, null=True)
    
    # Системные поля
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_processed = models.BooleanField(default=False, verbose_name="Обработана")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка №{self.id} от {self.created_at.strftime('%d.%m.%Y')}"