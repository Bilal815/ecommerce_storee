from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.models import TimeStampedModel, Extensions
from mptt.models import MPTTModel, TreeForeignKey
from djmoney.models.fields import MoneyField

# from .signals import post_signal

User = get_user_model()


class Newsletter(models.Model):
    """Newsletter Form Model"""
    serial_no = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class ContactForm(models.Model):
    """Contact Form Model"""
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='first_name', max_length=255, unique=False)
    email = models.EmailField(max_length=100, unique=False)
    message = models.CharField(max_length=255)
    newsletter = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)


def category_image_path(instance, filename):
    return "category/icons/{}/{}".format(instance.name, filename)


def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to=category_image_path, blank=True)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(Extensions):
    seller = models.ForeignKey(
        User, related_name="user_product", on_delete=models.CASCADE
    )
    category = TreeForeignKey(
        Category, related_name="product_category", on_delete=models.CASCADE
    )
    brand = models.CharField(default="Ludwin Dieter", max_length=100)
    manufacturer = models.CharField(default="Ludwin Dieter", max_length=100)
    title = models.CharField(max_length=250)
    oxygen = models.CharField(default="87", null=True, max_length=10)
    water = models.CharField(default="147 Dk/T", null=True, max_length=10)
    frequency = models.CharField(default="weekly", null=True, max_length=30)
    usage_desc = models.CharField(default="7 days usage", null=True, max_length=100)
    usage = models.CharField(default="Weekly", null=True, max_length=1000)
    gender = models.CharField(default="Uni-sex", null=True, max_length=10)
    year = models.IntegerField(default="2020", null=True, blank=True)
    upc = models.CharField(default="", null=True, max_length=20)
    tags = models.TextField(default="Random", null=True, blank=True)
    shape = models.CharField(default="square", null=True, max_length=30)
    style = models.CharField(default="Full Rim", null=True, max_length=20)
    uv = models.CharField(default="", null=True, max_length=20)
    progressive = models.BooleanField(default=False)
    customizable = models.BooleanField(default=False)
    frame_material = models.CharField(default="Acetate", null=True, max_length=20)
    lens_material = models.CharField(default="CR39", null=True, max_length=20)
    pd_range = models.CharField(default="61-85mm", null=True, max_length=20)
    presc_range = models.CharField(default="-7.00 ~ +7.00", null=True, max_length=20)
    age_range = models.CharField(default="", null=True, max_length=20)
    size = models.IntegerField(default=0)
    lens_color = models.TextField(default="Black", null=True, blank=True)
    color = models.TextField(default="Black", null=True, blank=True)
    marked_price = MoneyField(max_digits=10, default=0, decimal_places=2, default_currency='USD')
    price = MoneyField(max_digits=10, default=0, decimal_places=2, default_currency='USD')
    image = models.ImageField(upload_to=product_image_path, blank=True)
    image1 = models.ImageField(upload_to=product_image_path, blank=True)
    image2 = models.ImageField(upload_to=product_image_path, blank=True)
    image3 = models.ImageField(upload_to=product_image_path, blank=True)
    image4 = models.ImageField(upload_to=product_image_path, blank=True)
    details = models.TextField(null=True, blank=True)
    accessories = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    views = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.uuid), str(self.brand)
        """return self.name + str(self.uuid)"""


# @receiver(post_save, sender=Product)
# def create_index_elasticsearch(sender, instance, *args, **kwargs):
#     #post_signal(sender, instance)
#     from .serializers import ProductDocumentSerializer
#     serializer = ProductDocumentSerializer(instance)
#     try:
#         if serializer.is_valid():
#             serializer.save()
#             print("Product serializer saved w/ elasticsearch")
#     except Exception as e:
#         print("Product stuck at Elastic Search and not saved")
#         print(e)


class ProductViews(TimeStampedModel):
    ip = models.CharField(max_length=250)
    product = models.ForeignKey(
        Product, related_name="product_views", on_delete=models.CASCADE
    )


class Review(models.Model):
    """
    A review for a Product. If a Product is removed we should removed associated reviews
    """
    STARS_CHOICES = [(x, f"{x} Star") for x in range(1, 6)]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # keep reviews from deleted users
    stars = models.IntegerField(choices=STARS_CHOICES)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return '{} star: {}'.format(str(self.stars), str(self.comment))
