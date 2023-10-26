from django.db import models

# Create your models here.

# menu items
class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} | ${self.price}'