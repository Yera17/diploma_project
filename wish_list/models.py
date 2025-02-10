from django.contrib.auth.models import User
from products.models import Product
from django.db import models

class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class WishListItem(models.Model):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['wish_list', 'product'], name='unique_wishlist_product')
        ]

    def __str__(self):
        return self.product.name
