# Generated by Django 3.2.18 on 2024-07-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_subcategory_hot_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='hot_deal',
            field=models.BooleanField(default=False),
        ),
    ]
