# Generated by Django 3.2.18 on 2024-07-09 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_product_category_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_small_box',
            new_name='small_box_image',
        ),
    ]
