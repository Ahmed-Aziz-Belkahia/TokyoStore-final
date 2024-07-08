# Generated by Django 3.2.18 on 2024-07-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_product_is_recomended'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='outer_description',
            field=models.CharField(blank=True, help_text='Comma-separated list of available features', max_length=200),
        ),
    ]
