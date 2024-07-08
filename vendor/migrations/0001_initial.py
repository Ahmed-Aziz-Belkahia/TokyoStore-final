# Generated by Django 3.2.18 on 2024-07-05 07:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import shortuuid.django_fields
import userauths.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addons', '0002_contactus_product'),
        ('userauths', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryCouriers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couriers_name', models.CharField(max_length=1000)),
                ('couriers_tracking_website_address', models.URLField(blank=True, null=True)),
                ('did', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Delivery Couriers',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_cover_image', models.ImageField(blank=True, default='shop-cover-image.jpg', null=True, upload_to=userauths.models.user_directory_path)),
                ('shop_image', models.ImageField(blank=True, default='shop-image.jpg', null=True, upload_to=userauths.models.user_directory_path)),
                ('shop_name', models.CharField(blank=True, help_text='Shop Name', max_length=100, null=True)),
                ('shop_description', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True)),
                ('shop_policy', django_ckeditor_5.fields.CKEditor5Field(blank=True, default='', null=True)),
                ('shop_email', models.CharField(default='', max_length=150)),
                ('show_email_address_in_store', models.BooleanField(default=True, null=True)),
                ('show_mobile_number_in_store', models.BooleanField(default=True, null=True)),
                ('identity_image', models.ImageField(blank=True, default='id.jpg', null=True, upload_to=userauths.models.user_directory_path)),
                ('identity_type', models.CharField(blank=True, choices=[('national_id_card', 'National ID Card'), ('drivers_licence', 'Drives Licence'), ('international_passport', 'International Passport')], default='national_id_card', max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, default='', max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')], default='USD', max_length=40)),
                ('payout_method', models.CharField(choices=[('payout_to_paypal', 'Payout to Paypal'), ('payout_to_stripe', 'Payout to Stripe'), ('payout_to_wallet', 'Payout to Wallet')], default='payout_to_wallet', max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('paypal_email_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total_payout_tracker', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('stripe_access_token', models.CharField(blank=True, max_length=10000, null=True)),
                ('stripe_user_id', models.CharField(blank=True, max_length=10000, null=True)),
                ('stripe_refresh_token', models.CharField(blank=True, max_length=10000, null=True)),
                ('keywords', models.CharField(blank=True, help_text='Add keywords related to your shop, this would help buyers locate your shop', max_length=1000, null=True)),
                ('password', models.CharField(blank=True, max_length=10000, null=True)),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_country', to='addons.taxrate')),
                ('followers', models.ManyToManyField(blank=True, related_name='vendor_followers', to=settings.AUTH_USER_MODEL)),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_profile', to='userauths.profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vendors',
            },
        ),
        migrations.CreateModel(
            name='PayoutTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(blank=True, default='USD', max_length=40, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.cartorder')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.vendor')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='OrderTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=5000, null=True)),
                ('location', models.CharField(blank=True, max_length=5000, null=True)),
                ('activity', models.CharField(blank=True, max_length=5000, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('order_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartorderitem_tracker', to='store.cartorderitem')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('type', models.CharField(choices=[('new_order', 'New Order'), ('new_offer', 'New Offer'), ('new_bidding', 'New Bidding'), ('item_arrived', 'Item Arrived'), ('item_shipped', 'Item Shipped'), ('item_delivered', 'Item Delivered'), ('tracking_id_added', 'Tracking ID Added'), ('tracking_id_changed', 'Tracking ID Changed'), ('offer_rejected', 'Offer Rejected'), ('offer_accepted', 'Offer Accepted'), ('product_published', 'Product Published'), ('product_rejected', 'Product Rejected'), ('product_disabled', 'Product Disabled')], default='new_order', max_length=100)),
                ('seen', models.BooleanField(default=False)),
                ('nid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('bid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.productbidders')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.productoffers')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.cartorder')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_user', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_user', to='vendor.vendor')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('Percentage', 'Percentage'), ('Flat Rate', 'Flat Rate')], default='Percentage', max_length=100)),
                ('discount', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('redemption', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('make_public', models.BooleanField(default=False)),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('used_by', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupon_vendor', to='vendor.vendor')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=10000000000)),
                ('is_read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=25, prefix='')),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
