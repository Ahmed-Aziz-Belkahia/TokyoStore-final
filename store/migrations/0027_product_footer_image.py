# Generated by Django 3.2.18 on 2024-07-09 15:45

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_product_home_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='footer_image',
            field=models.ImageField(default='product.png', upload_to=userauths.models.user_directory_path),
        ),
    ]
