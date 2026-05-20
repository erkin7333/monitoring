from django.contrib import admin
from .models import Product, MonthlyPrice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(MonthlyPrice)
class MonthlyPriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "year",
        "month",
        "price"
    )

    list_filter = (
        "year",
        "month",
        "product__category"
    )

    search_fields = ("product__name",)