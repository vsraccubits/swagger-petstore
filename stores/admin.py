from django.contrib import admin

from stores.models import Address, Customer, Order


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "state", "zip")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("pet", "quantity", "ship_date", "status", "complete")


admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
