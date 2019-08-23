from django.db import models


class Products(models.Model):
    """
    This model will mapping to default database
    """
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.ImageField()
