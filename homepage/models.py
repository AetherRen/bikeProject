from django.db import models


# User Model
class User(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # date = models.DateField()

    def __str__(self):
        return self.name


# Bike System Model
class MySystem(models.Model):
    location = models.IntegerField(default=0)
    url = models.URLField()

    def __str__(self):
        return self.location


