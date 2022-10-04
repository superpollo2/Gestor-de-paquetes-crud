from django.urls import path
from .import views

urlpatterns = [
    path('nuevoenvio/',views.newShipping , name="new-shipping" ),
    path('',views.index,name="index"),
    path('envio/modificar/', views.shippingCrud, name="shipping-crud"), 
    path('usuario/modificar/', views.userCrud, name="user-crud"),
    path('usuario/trazabilidad/', views.trazabilidad, name="trazabilidad"), 
    
    
]
