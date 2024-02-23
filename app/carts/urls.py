from django.urls import path
from .views import *

app_name = 'carts'

urlpatterns = [
    path('cart-add/<slug:product_slug>/', cart_add, name='cart_add'),
    path('cart-change/<slug:product_slug>/', cart_change, name='cart_change'),
    path('cart-remove/<slug:product_slug>/', cart_remove, name='cart_remove'),
    
]
