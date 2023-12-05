from django.contrib import admin
from .models import Mobile, Laptop, Client, Seller, Order, Tv, Furniture, Refrigerator, Gas, T_shirt, pants


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'price', 'product')

admin.site.register(Mobile)
admin.site.register(Laptop)
admin.site.register(Client)
admin.site.register(Seller)
admin.site.register(T_shirt)
admin.site.register(pants)
admin.site.register(Tv)
admin.site.register(Gas)
admin.site.register(Furniture)
admin.site.register(Refrigerator)
admin.site.register(Order, OrderAdmin)

