# this modal will inherit from the something that already exist(The other class)
from django.db import models


# Here we will create a class to define our movie structure ...

class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
