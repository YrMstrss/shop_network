from django.db import models


class Contact(models.Model):
    pass


class Product(models.Model):
    pass


class Company(models.Model):
    class LinkType(models.TextChoices):
        factory = 'Factory', 'Завод'
        company = 'Company', 'ИП'
        retail = 'Retail', 'Розничная сеть'

    link_type = models.CharField(max_length=7, choices=LinkType.choices, verbose_name='тип звена сети')
    name = models.CharField(max_length=30, verbose_name='название')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакты')
    products = models.ManyToManyField(Product, blank=True, verbose_name='продукты')
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    level = models.IntegerField(default=0, verbose_name='уровень иерархии')

    def __str__(self):
        return f'ИП "{self.name}"'

    class Meta:
        verbose_name = 'ИП'
        verbose_name_plural = 'ИП'
