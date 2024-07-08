# Generated by Django 3.2.18 on 2024-07-05 07:57

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
import userauths.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addons', '0002_contactus_product'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gz_coins', models.IntegerField(blank=True, default=0, null=True)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('roles', models.CharField(blank=True, max_length=100, null=True)),
                ('total_spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('billing_first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_email', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_phone', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=500, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz123', length=7, max_length=25, prefix='')),
                ('cover_image', models.ImageField(blank=True, default='cover.jpg', null=True, upload_to=userauths.models.user_directory_path)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to=userauths.models.user_directory_path)),
                ('full_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('about_me', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=1000, null=True)),
                ('identity_type', models.CharField(blank=True, choices=[('national_id_card', 'National ID Card'), ('drivers_licence', 'Drives Licence'), ('international_passport', 'International Passport')], default='national_id_card', max_length=100, null=True)),
                ('identity_image', models.ImageField(blank=True, default='id.jpg', null=True, upload_to=userauths.models.user_directory_path)),
                ('facebook', models.URLField(blank=True, default='https://facebook.com/', null=True)),
                ('instagram', models.URLField(blank=True, default='https://instagram.com/', null=True)),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/', null=True)),
                ('whatsApp', models.CharField(blank=True, default='+123 (456) 789', max_length=100, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('seller', models.BooleanField(default=False)),
                ('subscribed_newsletter', models.BooleanField(default=False)),
                ('referral_earning', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('account_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=25, prefix='')),
                ('pin', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=6, prefix='')),
                ('code', models.CharField(blank=True, max_length=12, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_country_tax', to='addons.taxrate')),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ref_by', to=settings.AUTH_USER_MODEL)),
                ('saved_product', models.ManyToManyField(blank=True, to='store.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
