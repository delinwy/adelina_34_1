from django.contrib import admin

from post.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price']
    list_editable = ['product_price']
    list_filter = ['categories']
    list_per_page = 10
    search_fields = ['categories__description']


admin.site.register(Category)


