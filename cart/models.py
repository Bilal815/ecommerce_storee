from django.db import models
from products.models import Product
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class Cart(TimeStampedModel):
    user = models.OneToOneField(
        User, related_name="user_cart", on_delete=models.CASCADE
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True
    )


@receiver(post_save, sender=User)
def create_user_cart(sender, created, instance, *args, **kwargs):
    if created:
        Cart.objects.create(user=instance)


class CartItem(TimeStampedModel):
    cart = models.ForeignKey(Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="cart_product", on_delete=models.CASCADE
    )
    custom_order = models.BooleanField(default=False)
    pd_1 = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    pd_2 = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    right_sph = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    right_cyl = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    right_axis = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    right_add = models.CharField(default="None", null=True, max_length=100)
    left_sph = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    left_cyl = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    left_axis = models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)
    left_add = models.CharField(default="None", null=True, max_length=100)
    prism = models.BooleanField(default=False)
    lens_type = models.CharField(default="None", null=True, max_length=25)
    rx_type = models.CharField(default="None", null=True, max_length=25)
    lens_coat = models.CharField(default="None", null=True, max_length=25)
    quantity = models.IntegerField(default=1)

