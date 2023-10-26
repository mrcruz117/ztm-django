from django.db import models

# Create your models here.

# menu items


class Source_location(models.Model):

    address = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.address


class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    source = models.ForeignKey(
        Source_location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    favorite_item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.user_name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Users'
