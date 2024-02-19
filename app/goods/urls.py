from django.urls import path
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('product/<slug:slug>/', product, name='product'),
]
