from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
