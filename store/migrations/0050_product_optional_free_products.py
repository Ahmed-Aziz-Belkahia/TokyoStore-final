# Generated by Django 3.2.18 on 2024-09-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_alter_product_highlight_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='optional_free_products',
            field=models.ManyToManyField(blank=True, null=True, to='store.Product'),
        ),
    ]
