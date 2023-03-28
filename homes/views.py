from django.shortcuts import render,redirect
from .models import*
from .form import XarajatlarForm,IshxaqiForm
import requests
import datetime
def homes(request):
    
    return render(request,'ul_nor/dashboard.html')


def xarajat(request):
    xarajat=Xarajatlar.objects.all().order_by('-id')[0:10]
    profil=request.user.id
    print(profil)
    form=XarajatlarForm()
    if request.method == "POST":
        forms=XarajatlarForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('xarajat')
    
    context={"form":form,"xarajat":xarajat}
    return render(request,'ul_nor/Xarajat.html',context)


def ishxaqi(request):
    
    ishxaqqi=IshxaqiXarajati.objects.all().order_by('-id')[0:10]
    form=IshxaqiForm()
    if request.method == "POST":
        forms=IshxaqiForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('ishxaqi')
    
    context={"form":form,"ishxaqqi":ishxaqqi}
    return render(request,'ul_nor/ishxaqi.html',context)    

def valyuta(request):
    
    url1=f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/USD/{datetime.datetime}/ '
    url2=f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/RUB/{datetime.datetime}/ '
    url3=f'https://cbu.uz/ru/arkhiv-kursov-valyut/json/EUR/{datetime.datetime}/ '
    r1=(requests.get(url1)).json()
    r2=(requests.get(url2)).json()
    r3=(requests.get(url3)).json()
    
    ishxaqqi=IshxaqiXarajati.objects.all().order_by('-id')[0:10]
    form=IshxaqiForm()
    if request.method == "POST":
        forms=IshxaqiForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('ishxaqi')
    
    context={"form":form,"ishxaqqi":ishxaqqi,"r1":r1,"r2":r3,"r3":r2}
    return render(request,'ul_nor/valyuta.html',context)    

    