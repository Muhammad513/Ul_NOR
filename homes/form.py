from .models import*
from django import forms
from django.contrib.auth.models import User

x=datetime.datetime.now()
date=x.strftime("%Y-%m-%d")


class XarajatlarForm(forms.ModelForm):
   
    class Meta:
        model=Xarajatlar
        fields=('date',"name",'summ','comment','manba')
        widgets={
            'date':forms.TextInput(attrs={'type':'date','value':date}),
            'comment':forms.Textarea(attrs={'rows':'2'})
        }
    