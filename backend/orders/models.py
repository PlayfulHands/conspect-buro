from django.db import models

class Order(models.Model):
    WORK_TYPE_CHOICES = [
        ('conspect', 'Конспект'),
    ]
    
    FORMAT_CHOICES = [
        ('A4_tetrad', 'Тетрадь А4'),
        ('A5_tetrad', 'Тетрадь А5'),
        ('A4_list', 'Лист А4'),
    ]
    
    HANDWRITING_CHOICES = [
        ('any', 'Не имеет значения'),
        ('readable', 'Разборчивый почерк'),
        ('individual', 'Индивидуальный подбор'),
    ]
    
    HAS_MATERIAL_CHOICES = [
        ('yes', 'Есть готовый материал'),
        ('soon', 'Скоро появится'),
    ]
    
    GET_TYPE_CHOICES = [
        ('pickup', 'Заберу сам'),
        ('delivery', 'Нужна доставка'),
    ]

    vk_link = models.URLField(verbose_name="Ссылка ВКонтакте")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, default='conspect')
    pages = models.PositiveIntegerField(verbose_name="Объем работы (стр.)")
    deadline = models.DateField(verbose_name="Срок сдачи")
    paper_format = models.CharField(max_length=20, choices=FORMAT_CHOICES, verbose_name="Формат")
    handwriting = models.CharField(max_length=20, choices=HANDWRITING_CHOICES, verbose_name="Почерк")
    has_material = models.CharField(max_length=5, choices=HAS_MATERIAL_CHOICES, verbose_name="Материал")
    has_tables = models.BooleanField(default=False, verbose_name="Таблицы")
    has_schemes = models.BooleanField(default=False, verbose_name="Схемы")
    has_drawings = models.BooleanField(default=False, verbose_name="Рисунки")
    text_only = models.BooleanField(default=False, verbose_name="Только текст")
    additional_info = models.TextField(blank=True, verbose_name="Дополнительная информация")
    get_type = models.CharField(max_length=20, choices=GET_TYPE_CHOICES, verbose_name="Способ получения")
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ориентировочная цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_processed = models.BooleanField(default=False, verbose_name="Обработана")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка №{self.id} от {self.created_at.strftime('%d.%m.%Y')}"