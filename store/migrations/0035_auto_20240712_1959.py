# Generated by Django 3.2.18 on 2024-07-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_product_home_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitem',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
