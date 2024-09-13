from django.db import models

# Create your models here.


class Car(models.Model):
    name1 = models.CharField(max_length=3000)
    price = models.CharField(max_length=3000)
    date_added = models.CharField(max_length=3000)
    city = models.CharField(max_length=3000, blank=True, null=True)
    km_worked = models.CharField(max_length=3000)
    details = models.CharField(max_length=3000, null=True, blank=True)
    link = models.CharField(max_length=3000, unique=True)
    link2 = models.CharField(max_length=3000, blank=True, null=True)
    image = models.CharField(max_length=3000)

    def __str__(self):
        return f'{self.name1}'
