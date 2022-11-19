from django.db import models

# Create your models here.


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    supplier_address = models.CharField(max_length=100)
    # shops_detail = models.ForeignKey('api.Shop', on_delete = models.CASCADE, null=True)
    shop_detail = models.ManyToManyField('api.Shop', null=True, related_name='shop_detail')
    
    def __str__(self):
        return self.supplier_name
    
    
class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)   
    
    def __str__(self) :
        return self.shop_name
    
    
    

    
    
    
    
    

