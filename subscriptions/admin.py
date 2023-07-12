from django.contrib import admin
from .models import Subscription
# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'description',
    )


admin.site.register(Subscription, SubscriptionAdmin)
