from django.db import models
from jsonfield import JSONField


class CartCheckout(models.Model):
    email = models.EmailField()
    battletag = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    cart_items = models.TextField()
