from django.contrib.auth.models import User
from products.models import ProductSize
from django.db import models

class Bag(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class BagItem(models.Model):
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE)
    productSize = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.productSize.product.name
