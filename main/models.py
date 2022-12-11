from django.db import models

from django.db import models
from django.contrib.auth.models import User


###VERİTABANI MODELLERİ
class Data(models.Model):
    uuid = models.UUIDField( unique=True, editable=False , null=True , blank = True)
    KULLANICI = models.ForeignKey(User , blank=True , null=True , on_delete = models.CASCADE)
    
    TARIH = models.DateField(null=True , blank=True)
    ASIN = models.CharField(max_length=100 , null=True ,  blank=True)
    ALICI_SIPARIS_NUMARASI = models.CharField(max_length=100 , null=True,  blank=True)
    SATICI_SIPARIS_NUMARASI = models.CharField(max_length=100,null=True, blank=True)
    SATIS_FIYATI = models.FloatField(blank=True , null=True)
    AMAZON_FEE = models.FloatField(blank=True ,null=True)
    MALIYET = models.FloatField(blank=True , null=True)
    KAR = models.FloatField(blank=True , null=True)
    YUZDELIK_KAR = models.FloatField(blank=True , null=True)
    
    def __str__(self):
        return self.SATICI_SIPARIS_NUMARASI
class excelData(models.Model):
    file = models.FileField(upload_to="uploads/")

