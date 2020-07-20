from django.db import models


class Movie(models.Model):
    title        = models.CharField(max_length=200)
    length       = models.PositiveIntegerField()
    relase_year  = models.PositiveIntegerField()
    

    def __str__(self):
        return self.title 


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)
    phone      = models.PositiveIntegerField()



