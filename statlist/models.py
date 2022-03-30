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



class Club(models.Model):
    clubID = models.AutoField(primary_key=True)
    clubName = models.CharField(max_length=200)
    clubLogo = models.URLField(max_length=1000)

    def __str__(self):
        return f"{self.clubName}"

class Skills(models.Model):
    skillsID = models.AutoField(primary_key=True)
    prefferedFoot = models.CharField(max_length=10)
    pace = models.IntegerField(default=0)
    shooting = models.IntegerField(default=0)
    passing = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)
    defending = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.rating}, {self.prefferedFoot}"

class TransferMarket(models.Model):
    transferID = models.AutoField(primary_key=True)
    value = models.CharField(max_length=10, null=True)
    contractExpiry = models.IntegerField()
    wages = models.CharField(max_length=10)
    releaseClause = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.value, self.wages, self.releaseClause, self.contractExpiry}"
