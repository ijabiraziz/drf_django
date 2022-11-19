from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('shop/<str:name>', views.shop_list, name="shop_list"),
    path('supplier/<int:id>', views.supplier_no_of_shops, name="supplier_no_of_shops")

    
]
