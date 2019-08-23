from djongo import models


class Order(models.Model):
    """
    This model will mapping to mongo database
    """
    order_name = models.CharField(max_length=50)
    invoice = models.FloatField()
