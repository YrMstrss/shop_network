from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    model = models.CharField(max_length=50, verbose_name='модель')
    start_sales_date = models.DateField(auto_now_add=True, verbose_name='дата начала продаж')

    def __str__(self):
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Link(models.Model):
    class LinkType(models.TextChoices):
        factory = 'Factory', 'Завод'
        company = 'Company', 'ИП'
        retail = 'Retail', 'Розничная сеть'

    link_type = models.CharField(max_length=7, choices=LinkType.choices, verbose_name='тип звена сети')
    name = models.CharField(max_length=30, verbose_name='название')
    products = models.ManyToManyField(Product, blank=True, verbose_name='продукты')
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', blank=True, null=True)
    debt = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    level = models.IntegerField(default=0, verbose_name='уровень иерархии')

    def __str__(self):
        return f'Звено сети "{self.name}"'

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'


class Contact(models.Model):
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    building = models.CharField(max_length=5, verbose_name='номер дома')

    link = models.OneToOneField(Link, on_delete=models.CASCADE, related_name='contact', verbose_name='звено', null=True, blank=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'
