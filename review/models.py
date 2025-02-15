from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

from products.models import Product


# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.FloatField(
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        default=1.0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return self.user.username