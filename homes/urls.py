from django.urls import path,include
from .views import homes

urlpatterns = [
    path('',homes,name='home'),
    
]
