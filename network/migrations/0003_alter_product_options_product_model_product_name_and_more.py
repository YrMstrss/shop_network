# Generated by Django 5.0.1 on 2024-01-09 19:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_contact_options_contact_building_contact_city_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default=1, max_length=50, verbose_name='модель'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='start_sales_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата начала продаж'),
            preserve_default=False,
        ),
    ]
