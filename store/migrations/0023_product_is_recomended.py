# Generated by Django 3.2.18 on 2024-07-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_product_in_pack'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_recomended',
            field=models.BooleanField(default=False),
        ),
    ]
