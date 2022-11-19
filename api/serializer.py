from rest_framework import serializers
from .models import Shop, Supplier


class ShopSerailzer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Shop
        # fields = '__all__'
        exclude = ['id']
        
        
class SupplierSerailzer(serializers.ModelSerializer):
    shop_detail = ShopSerailzer(many=True, read_only=True)
    
    class Meta:
        model = Supplier
        # fields = '__all__'
        fields = ['supplier_name','supplier_address','shop_detail']
        
        
        
