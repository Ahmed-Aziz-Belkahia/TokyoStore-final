# Generated by Django 3.2.18 on 2024-09-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_auto_20240912_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.CharField(help_text='Comma-separated list of available colors', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, default='x', help_text='Comma-separated list of available sizes', max_length=200),
            preserve_default=False,
        ),
    ]