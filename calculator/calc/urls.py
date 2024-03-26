from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the root URL ==> DON'T DELETE IT
    path('', views.calculate, name='calculate'),  
    path('calculate',views.calculate,name='calculate'),
]
