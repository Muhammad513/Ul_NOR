from django.shortcuts import render,redirect
from .form import XarajatForm

def homes(request):
    
    return render(request,'ul_nor/dashboard.html')


def xarajat(request):
    user=request.user.id
    form=XarajatForm(user)
    if request.method == "POST":
        forms=XarajatForm(user,request.POST)
        if forms.is_valid():
            formsets=forms.save(commit=False)
            formsets.user=user
            formsets.save()
            return redirect('xarajat')
    
    context={"form":form}
    return render(request,'ul_nor/Xarajat.html',context)