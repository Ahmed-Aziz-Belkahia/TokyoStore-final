# Generated by Django 3.2.18 on 2024-07-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_product_footer_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='deal_image',
            field=models.ImageField(blank=True, default='deal.png', null=True, upload_to='deal'),
        ),
    ]