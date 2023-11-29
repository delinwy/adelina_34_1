from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=500, null=True)
    product_rate = models.FloatField(default=0)
    product_price = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_name}'


