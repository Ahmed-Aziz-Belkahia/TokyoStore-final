# Generated by Django 3.2.18 on 2024-09-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_auto_20240908_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalchoice',
            name='general_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general_choices', to='store.type'),
        ),
    ]
