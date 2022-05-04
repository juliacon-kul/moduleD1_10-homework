from django.db import models

# Create your models here.

class Auto(models.Model):
    manufacturer = models.CharField(max_length=100)
    slug = models.SlugField
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    TRANSMISSION_CHOICES = [
        (1, 'механика'),
        (2, 'автомат'),
        (3, 'робот'),
    ]
    transmission = models.SmallIntegerField(
        choices=TRANSMISSION_CHOICES,
        default=1,)
    colour = models.CharField(max_length=100)


    def __str__(self):
        return self.manufacturer+" "+self.model


