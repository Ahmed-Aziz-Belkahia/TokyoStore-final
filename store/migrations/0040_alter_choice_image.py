# Generated by Django 3.2.18 on 2024-09-06 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_alter_social_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.gallery'),
        ),
    ]