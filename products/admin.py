from django.contrib import admin
from .models import Product, Category, Subscription


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'description',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
