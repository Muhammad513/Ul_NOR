from django.shortcuts import render


def homes(request):
    
    return render(request,'ul_nor/dashboard.html')
