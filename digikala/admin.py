from django.contrib import admin

from .models import (
    Client,
    Furniture,
    Gas,
    Laptop,
    Mobile,
    Order,
    Refrigerator,
    Seller,
    T_shirt,
    Tv,
    pants,
)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "price")
    list_filter = ("customer", "product")
    search_fields = ("customer", "price", "product")


class LaptopAdmin(admin.ModelAdmin):
    search_fields = ("name", "ram", "cpu_model")
    list_display = ("name", "price", "ram", "cpu_model")
    list_filter = ("name", "ram", "cpu_model", "screan_size", "webcam")


class GasAdmin(admin.ModelAdmin):
    search_fields = ("name", "gas_type", "quality", "flame_number")
    list_display = ("name", "price", "gas_type", "quality", "flame_number")
    list_filter = ("name", "gas_type", "quality", "flame_number")


class TvAdmin(admin.ModelAdmin):
    search_fields = ("name", "quality")
    list_display = ("name", "price", "quality", "technology")
    list_filter = ("name", "quality", "technology")


class MobileAdmin(admin.ModelAdmin):
    search_fields = ("name", "cpu", "ram", "sim_number", "camera", "os")
    list_display = ("name", "price", "cpu", "ram")
    list_filter = ("name", "price", "cpu", "ram", "sim_number", "camera", "os")


class ClientAdmin(admin.ModelAdmin):
    search_fields = ("user", "name", "phone_number", "zip_code")
    list_filter = ("user", "name", "phone_number", "zip_code")
    list_display = ("user", "name", "phone_number")


class SellerAdmin(admin.ModelAdmin):
    search_fields = ("user", "name", "phone_number", "products_varity")
    list_display = ("user", "name", "phone_number", "products_varity", "score")
    list_filter = ("user", "name", "phone_number", "products_varity", "score")


class RefrigeratorAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "power_usage",
    )
    list_filter = ("name", "power_usage", "capacity_litre")
    list_display = ("name", "price", "power_usage", "capacity_litre")


class FurnitureAdmin(admin.ModelAdmin):
    search_fields = ("name", "material_body")
    list_display = ("name", "price", "material_body", "Capacity")
    list_filter = ("name", "material_body", "Capacity")


class pantsAdmin(admin.ModelAdmin):
    search_fields = ("name", "size", "material", "style", "gender")
    list_display = (
        "name",
        "price",
        "crotch",
        "size",
        "material",
        "style",
        "gender",
    )
    list_filter = ("name", "size", "crotch", "material", "style", "gender")


class T_shirtAdmin(admin.ModelAdmin):
    search_fields = ("name", "size", "material", "style", "gender")
    list_display = (
        "name",
        "price",
        "Sleeve",
        "size",
        "material",
        "style",
        "gender",
    )
    list_filter = ("name", "size", "Sleeve", "material", "style", "gender")


admin.site.register(Mobile, MobileAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(T_shirt, T_shirtAdmin)
admin.site.register(pants, pantsAdmin)
admin.site.register(Tv, TvAdmin)
admin.site.register(Gas, GasAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Refrigerator, RefrigeratorAdmin)
admin.site.register(Order, OrderAdmin)
