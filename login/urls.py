from django.urls import path,include
from .views import loginPage,logoutUser

urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
]
