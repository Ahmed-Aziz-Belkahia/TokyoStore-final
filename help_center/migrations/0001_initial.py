# Generated by Django 3.2.18 on 2024-07-05 07:57

from django.db import migrations, models
import shortuuid.django_fields
import taggit.managers
import userauths.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=userauths.models.user_directory_path)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('closed', 'Closed'), ('in_review', 'In Review'), ('published', 'Published')], default='published', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('answer_status', models.CharField(choices=[('Answered', 'Answered'), ('Not Answered', 'Not Answered')], default='Not Answered', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('category', models.ManyToManyField(blank=True, to='help_center.Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
