from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','description', 'created_at', 'updated_at']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'price','image_tag', 'category', 'created_at', 'updated_at']

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return 'No Image'

    image_tag.short_description = 'Image'

admin.site.register(Product, ProductAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_email', 'product',  'quantity','created_at', 'updated_at']