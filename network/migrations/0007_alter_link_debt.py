# Generated by Django 5.0.1 on 2024-01-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_remove_link_contact_contact_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='задолженность перед поставщиком'),
        ),
    ]
