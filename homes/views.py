from django.shortcuts import render,redirect
from .models import*
from .form import XarajatlarForm

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