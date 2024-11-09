from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","category_list",)
    search_fields = ("name","categories",)
    list_filter = ("isActive","categories",)

    def category_list(self, product):
        category_list = ""
        for category in product.categories.all():
            category_list += category.name + " / "
        return category_list
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","product_count")
    search_fields = ("name",)

    def product_count(self, category):
        return category.product_set.count()