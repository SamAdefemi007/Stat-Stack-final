from operator import truediv
from django.db import models

# Create your models here.


class Country(models.Model):
    countryID = models.AutoField(primary_key=True)
    countryName = models.CharField(max_length=200)
    countryFlag = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.countryName}"

    class Meta:
        ordering = ('countryName',)