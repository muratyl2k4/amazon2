from django.db import models

class Deneme(models.Model):
    name= models.CharField(max_length=100)