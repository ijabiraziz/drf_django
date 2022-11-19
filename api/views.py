from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Shop, Supplier
from .serializer import ShopSerailzer, SupplierSerailzer
from .filters import ShopFilter
import json


# Create your views here.


"""Get all the suppliers and associated shops"""
@api_view(['GET'])
def index(request):
    supplier = Supplier.objects.all()
    serializer = SupplierSerailzer(supplier, many=True)
    return Response(serializer.data)



"""Get a specific shops by entering shop name or any substring,
by navigating to http://localhost:8000/shop/(ShopName)"""
@api_view(['GET'])
def shop_list(request,name):
    queryset = Shop.objects.filter(shop_name__icontains=name)
    # shop_supplier = Shop.account_set.all()
    serializer = ShopSerailzer(queryset, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def supplier_no_of_shops(request,id):
    queryset = Supplier.objects.get(pk=id) 
    count_shops = queryset.shop_detail.all().count()
    

    return HttpResponse(f"<b>{queryset}</b> Supply to <b> {count_shops}</b> shops.")
