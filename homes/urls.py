from django.urls import path,include
from .views import homes,xarajat,ishxaqi,valyuta

urlpatterns = [
    path('',homes,name='home'),
    path('xarajat/',xarajat,name='xarajat'),
    path('ishxaqi/',ishxaqi,name='ishxaqi'),
    path('valyuta/',valyuta,name='valyuta')
    
]
