from .models import*
from django import forms
from django.contrib.auth.models import User




class XarajatForm(forms.ModelForm):
    
    class Meta:
        model=Xarajatlar
        fields='__all__'    
       

    