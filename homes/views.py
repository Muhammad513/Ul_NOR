from django.shortcuts import render,redirect
from .models import*
from .form import XarajatlarForm,IshxaqiForm

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