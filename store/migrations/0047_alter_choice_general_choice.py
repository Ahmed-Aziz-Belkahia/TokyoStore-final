# Generated by Django 3.2.18 on 2024-09-08 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_auto_20240908_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='general_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='store.generalchoice'),
        ),
    ]
