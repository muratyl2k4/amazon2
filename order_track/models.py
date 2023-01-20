from django.db import models
from main.models import Data

class Order(models.Model):

    Order = models.ForeignKey(Data , null=True , blank=True , on_delete=models.CASCADE)
    Tracknumber = models.CharField(max_length=200 , null=True , blank=True)
    Courier_Name = models.CharField(max_length=200 , null=True , blank=True)
    Last_Status = models.CharField(max_length=500 , null=True , blank=True)
    Last_Update = models.DateField(null=True , blank=True)

    def __str__(self):
        return self.Tracknumber

