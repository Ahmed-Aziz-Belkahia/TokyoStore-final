# Generated by Django 3.2.18 on 2024-09-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_auto_20240908_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='general_meta_title',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='general_title',
        ),
        migrations.CreateModel(
            name='generalChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_title', models.SlugField(blank=True, null=True, unique=True)),
                ('general_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_choices', to='store.type')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='general_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='store.generalchoice'),
        ),
    ]