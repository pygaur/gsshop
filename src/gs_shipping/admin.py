from django.contrib import admin

from .models import ShippingMethod


class ShippingMethodAdmin(admin.ModelAdmin):
    """
    """
    prepopulated_fields = {'code': ('name',), }


admin.site.register(ShippingMethod, ShippingMethodAdmin)
