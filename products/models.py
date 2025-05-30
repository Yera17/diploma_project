from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="products",on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    img_url = models.URLField()
    asin = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=False)
    total_in_stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name="sizes",on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=False)
    number_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.value