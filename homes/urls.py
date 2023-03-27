from django.urls import path,include
from .views import homes,xarajat,ishxaqi

urlpatterns = [
    path('',homes,name='home'),
    path('xarajat/',xarajat,name='xarajat'),
    path('ishxaqi/',ishxaqi,name='ishxaqi')
    
]
