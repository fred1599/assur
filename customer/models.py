from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    age = models.IntegerField()
