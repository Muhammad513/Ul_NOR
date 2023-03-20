from django.urls import path,include
from .views import homes,xarajat

urlpatterns = [
    path('',homes,name='home'),
    path('xarajat/',xarajat,name='xarajat'),

    
]
