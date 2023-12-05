from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Client(Person):
    zip_code = models.PositiveIntegerField()


class Seller(Person):
    PRODUCTS_VARITY = {
        ("clothing", "Clothing"),
        ("electronic device", "Electronic device"),
        ("home Appliances", "Home Appliances"),
    }

    products_varity = models.CharField(choices=PRODUCTS_VARITY, max_length=25)
    score = models.PositiveIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    # def __str__(self) -> str:
    #     return f"{self.customer}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="OrderItem"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Clothing(Product):
    GENDER = {("male", "Male"), ("female", "Female"), ("baby", "Baby")}

    STYLE = {("normal", "Normal"), ("classic", "Classic"), ("slash", "Slash")}

    MATERIAL = {
        ("cotton", "Cotton"),
        ("woolen", "Woolen"),
        ("silk", "Silk"),
        ("linen", "Linen"),
    }

    SIZE = {
        ("s", "S"),
        ("m", "M"),
        ("l", "L"),
        ("xl", "XL"),
    }

    material = models.CharField(choices=MATERIAL, max_length=10)
    gender = models.CharField(choices=GENDER, max_length=10)
    style = models.CharField(choices=STYLE, max_length=10)
    size = models.CharField(choices=SIZE, max_length=2)
    color = models.CharField(max_length=50)
    design = models.CharField(max_length=100)
    heigh = models.CharField(max_length=100)


class T_shirt(Clothing):
    SLEEVE_SIZE = {("long", "Long"), ("short", "Short")}

    Sleeve = models.CharField(choices=SLEEVE_SIZE, max_length=10)


class pants(Clothing):
    CROTCH = {("long", "Long"), ("short", "Short")}

    crotch = models.CharField(choices=CROTCH, max_length=10)


class HomeAppliance(Product):
    PLACE = {("kitchen", "Kitchen"), ("livingroom", "livingroom")}

    MATERIAL_BODY = {("wood", "Wood"), ("steal", "Steal")}

    place = models.CharField(choices=PLACE, max_length=20)


class KitchenAppliance(HomeAppliance):
    WORK_WITH = {("gas", "Gas"), ("electricity", "Electricity")}

    work_with = models.CharField(choices=WORK_WITH, max_length=20)


class Refrigerator(KitchenAppliance):
    POWER_USAGE = {("b", "B"), ("a", "A"), ("a+", "A+"), ("a++", "A++")}

    power_usage = models.CharField(choices=POWER_USAGE, max_length=3)
    capacity_litre = models.PositiveIntegerField()


class Gas(KitchenAppliance):
    QUALITY = {("steal", "Steal"), ("glass", "Glass")}

    GAS_TYPE = {("stove", "Stove"), ("sheet", "Sheet")}

    gas_type = models.CharField(choices=GAS_TYPE, max_length=5)
    quality = models.CharField(choices=QUALITY, max_length=5)
    flame_number = models.DecimalField(max_digits=5, decimal_places=2)


class Tv(HomeAppliance):
    QUALITY = {("HD", "HD"), ("FULLHD", "FULLHD"), ("4K", "4K")}

    quality = models.CharField(choices=QUALITY, max_length=6)
    technology = models.CharField(max_length=50, default="LED")


class Furniture(HomeAppliance):
    material_body = models.CharField(
        choices=HomeAppliance.MATERIAL_BODY, max_length=10
    )
    Capacity = models.DecimalField(max_digits=15, decimal_places=1)


class Electronicdevice(Product):
    USE_FOR = {
        ("office", "Office"),
        ("student", "Student"),
        ("work", "Work"),
        ("game", "Game"),
    }

    model = models.CharField(max_length=150)
    use_for = models.CharField(choices=USE_FOR, max_length=10)
    storage_by_M = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class Laptop(Electronicdevice):
    RESOLUTION = {
        ("1280×720", "1280×720"),
        ("1920×1080", "1920×1080"),
        ("3840×2160", "3840×2160"),
    }

    ram = models.PositiveIntegerField()
    cpu_model = models.CharField(max_length=150)
    number_core = models.PositiveIntegerField()
    resolution = models.CharField(choices=RESOLUTION, max_length=11)
    screan_size = models.FloatField()
    webcam = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Mobile(Electronicdevice):
    OS = {("android", "Android"), ("ios", "Ios")}

    screen_size = models.FloatField()
    cpu = models.CharField(max_length=200)
    ram = models.PositiveIntegerField()
    camera = models.PositiveIntegerField()
    os = models.CharField(choices=OS, max_length=10)
    sim_number = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
