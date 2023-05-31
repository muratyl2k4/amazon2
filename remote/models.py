from django.db import models
from django.contrib.auth.models import User

#TODO
#comda yoksa sadece asin
#buy?sale stok yok gec
class CompletedAbstract(models.Model):
    User = models.ForeignKey(User , blank=True , null=True , on_delete = models.CASCADE)
    Title= models.CharField(max_length=100,blank=True,null=True)
    Asin = models.CharField(max_length=100,blank=True,null=True)
    SalesRank = models.IntegerField(blank=True,null=True)
    Drop_Count = models.IntegerField(blank=True,null=True)
    Buy_Price = models.FloatField(blank=True,null=True)
    Sale_Price_BB = models.FloatField(blank=True,null=True)
    Sale_Price_FBM = models.FloatField(blank=True,null=True)
    Sale_Price_FBA= models.FloatField(blank=True,null=True)
    Sale_Price_NC = models.FloatField(blank=True,null=True)
    Ratio = models.FloatField(blank=True,null=True)
    Cost = models.FloatField(blank=True,null=True)
    Profit = models.FloatField(blank=True,null=True)
    Profit_Percentage = models.FloatField(blank=True,null=True)
    Sales_Info = models.IntegerField(blank=True,null=True)
    Date = models.DateField(blank=True,null=True)
    Fba_Seller_Count = models.IntegerField(blank=True,null=True)
    Is_Buybox_Fba = models.BooleanField(default = False ,blank=True,null=True)
    Is_Amazon_Selling = models.BooleanField(default=False ,blank=True,null=True)

    class Meta:
        abstract = True
    def __str__(self):
        return self.Asin

class NotCompletedAbstract(models.Model):
    Asin = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        abstract = True

class KeepaExcelAbstract(models.Model):
    Title= models.CharField(max_length=100,blank=True,null=True)
    Asin = models.CharField(max_length=100,blank=True,null=True)
    #hedef
    SalesRank = models.IntegerField(blank=True,null=True)
    Drop_Count = models.IntegerField(blank=True,null=True) 
    #com
    Buy_Price = models.FloatField(blank=True,null=True)
    #hedef
    Sale_Price_NC = models.FloatField(blank=True , null=True)
    Sale_Price_BB = models.FloatField(blank=True,null=True)
    Sale_Price_FBM = models.FloatField(blank=True,null=True)
    Sale_Price_FBA= models.FloatField(blank=True,null=True)
    #hedefusd/com
    Ratio = models.FloatField(blank=True,null=True) 
    class Meta:
        abstract = True

class CompletedUK(CompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(CompletedUK, self).__init__(*args, **kwargs)
        
class CompletedCA(CompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(CompletedCA, self).__init__(*args, **kwargs)

class CompletedJA(CompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(CompletedJA, self).__init__(*args, **kwargs)

class CompletedAU(CompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(CompletedAU, self).__init__(*args, **kwargs)

class CompletedFR(CompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(CompletedFR, self).__init__(*args, **kwargs)

class CompletedDE(CompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(CompletedDE, self).__init__(*args, **kwargs)

class NotCompletedUK(NotCompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(NotCompletedUK, self).__init__(*args, **kwargs)

class NotCompletedCA(NotCompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(NotCompletedCA, self).__init__(*args, **kwargs)

class NotCompletedJA(NotCompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(NotCompletedJA, self).__init__(*args, **kwargs)

class NotCompletedAU(NotCompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(NotCompletedAU, self).__init__(*args, **kwargs)

class NotCompletedFR(NotCompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(NotCompletedFR, self).__init__(*args, **kwargs)

class NotCompletedDE(NotCompletedAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(NotCompletedDE, self).__init__(*args, **kwargs)

class KeepaExcelUK(KeepaExcelAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(KeepaExcelUK, self).__init__(*args, **kwargs)

class KeepaExcelCA(KeepaExcelAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(KeepaExcelCA, self).__init__(*args, **kwargs)

class KeepaExcelJA(KeepaExcelAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(KeepaExcelJA, self).__init__(*args, **kwargs)

class KeepaExcelAU(KeepaExcelAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(KeepaExcelAU, self).__init__(*args, **kwargs)

class KeepaExcelFR(KeepaExcelAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(KeepaExcelFR, self).__init__(*args, **kwargs)

class KeepaExcelDE(KeepaExcelAbstract):
    def __init__(self, *args, **kwargs):
        for f in self._meta.fields:
            if f.attname == "parent_field":
                f.default = "child default"
        super(KeepaExcelDE, self).__init__(*args, **kwargs)
