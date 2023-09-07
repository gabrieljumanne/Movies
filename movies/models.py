# this modal will inherit from the something that already exist(The other class)
from django.db import models


# Here we will create a class to define our movie structure ...
# This is my database structure
# This modal represent a table in data base
# Each attribute represent a column of the table
class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    # Making the director field to be nullable ...since there are some existing rows
    director = models.CharField(max_length=200, null=True)

# To get the string representation we define the method
    def __str__(self):
        return f"{self.title} {self.year} {self.director}"


class Users(models.Model):
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    # for string representation in admin
    def __str__(self):
        return f"{self.firstName} {self.secondName} {self.role}"
