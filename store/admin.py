from django.contrib import admin
from django import forms
from store.models import (CallToActionBanner, CartOrderItem, Choice, Genre, Product, Category, CartOrder, Gallery,
                         Brand, ProductFaq, Review, ProductBidders, ProductOffers, SubCategory, Type, Specification,
                         SpecificationValue, Mapping, Social, generalChoice, generalType)
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import ModelChoiceField
from userauths.models import User, Profile


@admin.action(description="Mark selected products as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status="published")

@admin.action(description="Mark selected products as In Review")
def make_in_review(modeladmin, request, queryset):
    queryset.update(status="in_review")

@admin.action(description="Mark selected products as Featured")
def make_featured(modeladmin, request, queryset):
    queryset.update(featured=True)

class ProductImagesAdmin(admin.TabularInline):
    model = Gallery
    extra= 0

class SpecificationValueInline(admin.TabularInline):
    model = SpecificationValue
    extra= 0

class SpecificationInline(admin.TabularInline):
    model = Specification
    inlines = [SpecificationValueInline]
    extra= 0

class CartOrderItemsInlineAdmin(admin.StackedInline):
    model = CartOrderItem
    extra= 0

class StaffUserChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username

class ChoiceInlineForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Extract the instance from kwargs
        type_instance = kwargs.pop('type_instance', None)
        super().__init__(*args, **kwargs)

        if type_instance:
            # Filter general_choice dropdown based on the general_type of the Type instance
            self.fields['general_choice'].queryset = generalChoice.objects.filter(
                general_type=type_instance.general_type
            )

class TypesChoicesAdmin(admin.TabularInline):
    model = Choice
    form = ChoiceInlineForm
    prepopulated_fields = {"meta_title": ("title", )}
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        # Get the formset
        formset = super().get_formset(request, obj, **kwargs)
        # Override the formset’s form class to include the current Type instance
        class FormsetWithTypeInstance(formset):
            def __init__(self, *args, **kwargs):
                # Pass the current Type instance to the form
                if obj:
                    kwargs['form_kwargs'] = {'type_instance': obj}
                super().__init__(*args, **kwargs)
        return FormsetWithTypeInstance

    def get_form(self, request, obj=None, **kwargs):
        # Add the type instance to the form kwargs
        form = super().get_form(request, obj, **kwargs)
        if obj:
            # Inject type_instance into form kwargs
            form.base_fields['general_choice'].queryset = generalChoice.objects.filter(
                general_type=obj.general_type
            )
        return form

class generalTypesGeneralChoicesAdmin(admin.TabularInline):
    model = generalChoice
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class InlineType(admin.TabularInline):
    model = Type
    list_display = ['title']
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class TypeAdmin(ImportExportModelAdmin):
    inlines = [TypesChoicesAdmin]
    """ list_display = ['__str__'] """
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class generalTypeAdmin(ImportExportModelAdmin):
    inlines = [generalTypesGeneralChoicesAdmin]
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class ProductAdmin(ImportExportModelAdmin):
    inlines = [ProductImagesAdmin, InlineType, SpecificationInline]  # Added SpecificationInline
    search_fields = ['title', 'price']
    list_filter = ['featured', 'status', 'in_stock', 'type', 'vendor']
    list_editable = ['price', 'featured', 'status', 'shipping_amount', 'hot_deal', 'hero_section_featured']
    list_display = ['product_image' ,'title',  'price', 'featured', 'shipping_amount', 'in_stock' ,'stock_qty', 'order_count', 'vendor' ,'status', 'featured', 'hero_section_featured' ,'hot_deal']
    actions = [make_published, make_in_review, make_featured]
    list_per_page = 1300
    prepopulated_fields = {"slug": ("title", )}
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(is_staff=True)
            kwargs['form_class'] = StaffUserChoiceField
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['title', 'category_image']
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class SubCategoryAdmin(ImportExportModelAdmin):
    list_display = ['title', 'category_image']
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class GenreAdmin(ImportExportModelAdmin):
    list_display = ['title', 'genre_image']
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class CartOrderAdmin(ImportExportModelAdmin):
    inlines = [CartOrderItemsInlineAdmin]
    search_fields = ['oid', 'tracking_id', 'product__title']
    list_editable = ['order_status', 'payment_status' ,'delivery_status']
    list_filter = ['payment_status', 'order_status', 'delivery_status']
    list_display = ['oid', 'payment_status', 'order_status', 'delivery_status' ,'price', 'shipping', 'vat', 'service_fee' ,'total', 'saved' ,'email','date']
    extra= 0

class CartOrderItemsAdmin(ImportExportModelAdmin):
    search_fields = ['oid', 'tracking_id', 'product', 'coupon__code', 'order__oid', 'vendor__shop_name']
    list_filter = ['paid', 'paid_vendor', 'cancelled', 'delivery_couriers', 'applied_coupon']
    list_display = ['order',  'vendor' , 'order_img','product_obj' ,'qty', 'price', 'total', 'shipping' , 'service_fee', 'vat','total_payable', 'grand_total' , 'delivery_couriers' , 'paid', 'paid_vendor', 'applied_coupon' ,'cancelled']
    extra= 0

class BrandAdmin(ImportExportModelAdmin):
    list_editable = ['featured', 'active']
    list_display = ['title', 'brand_image', 'active', 'featured']
    prepopulated_fields = {"meta_title": ("title", )}
    extra= 0

class ProductFaqAdmin(ImportExportModelAdmin):
    list_editable = [ 'active', 'answer']
    list_display = ['user', 'question', 'answer' ,'active']
    extra= 0

class ProductBiddersAdmin(ImportExportModelAdmin):
    list_display = ['user', 'product', 'price','winner', 'win_status' ,'email']
    extra= 0

class ProductReviewAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['user', 'product', 'review', 'reply' ,'rating', 'active']
    extra= 0

class ProductOfferAdmin(ImportExportModelAdmin):
    list_display = ['user', 'product', 'price','status', 'email']
    extra= 0

class CallToActionBannerAdmin(ImportExportModelAdmin):
    list_editable = ["CTA_type"]
    list_display = ['banner_image', 'product', "CTA_type"]
    extra= 0

class SpecificationValueAdmin(admin.ModelAdmin):
    list_display = ['specification', 'title', 'description']
    list_filter = ['specification']
    extra= 0

class SpecificationAdmin(admin.ModelAdmin):
    inlines = [SpecificationValueInline]
    list_display = ['sid', 'product', 'title']
    search_fields = ['title']
    list_filter = ['product']
    extra= 0

admin.site.register(ProductBidders, ProductBiddersAdmin)
admin.site.register(Review, ProductReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItem, CartOrderItemsAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductFaq, ProductFaqAdmin)
admin.site.register(ProductOffers, ProductOfferAdmin)
admin.site.register(CallToActionBanner, CallToActionBannerAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(generalType, generalTypeAdmin)
admin.site.register(Specification, SpecificationAdmin)  # Added
admin.site.register(SpecificationValue, SpecificationValueAdmin)  # Added
admin.site.register(Mapping)  # Added
admin.site.register(Social)  # Added
