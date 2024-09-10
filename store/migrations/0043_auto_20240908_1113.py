# Generated by Django 3.2.18 on 2024-09-08 10:13

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_alter_type_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='generalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('meta_title', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='general_meta_title',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='general_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='add_to_filter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='social',
            name='image',
            field=models.ImageField(upload_to=store.models.preserve_filename),
        ),
        migrations.AddField(
            model_name='type',
            name='general_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='store.generaltype'),
        ),
    ]
