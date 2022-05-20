import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings.development")
django.setup()

from ecommerce.asgi import get_default_application

application = get_default_application()

from products.models import Product


# write script
def populate():
    user = Product()
    user.seller = "sunglasses"
    user.category = "0"
    user.brand = "Ludwin Dieter"
    user.manufacturer = "Ludwin Dieter"
    user.title = "udwin DieterL"
    user.oxygen = "87"
    user.water = "147 Dk/T"
    user.frequency = "weekly"
    user.usage_desc = "7 days usage"
    user.usage = "Weekly"
    user.gender = "Uni-sex"
    user.year = "2020"
    user.upc = "1213123112"
    user.tags = "Random"
    user.shape = "square"
    user.style = "Full Rim"
    user.uv = 3
    user.progressive = True
    user.customizable = True
    user.frame_material = "35-30mm"
    user.lens_material = "35-30mm"
    user.pd_range = "35-30mm"
    user.presc_range = "35-30mm"
    user.age_range = "20-35"
    user.size = "Blue"
    user.lens_color = "Blue"
    user.color = "Blue"
    user.marked_price =180
    user.selling_price = 150
    user.image1 = ""
    user.image2 = ""
    user.image3 = ""
    user.image4 = ""
    user.image5 = ""
    user.details = "Wooden Stick"
    user.accessories = "Wooden Stick"
    user.description = "Wooden Stick"
    user.quantity = 1
    user.save()


# end script
if __name__ == '__main__':
    populate()
