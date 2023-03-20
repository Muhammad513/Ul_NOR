from .models import*
from django import forms
from django.contrib.auth.models import User




class XarajatForm(forms.ModelForm):
    
    class Meta:
        model=Xarajatlar
        fields='__all__'    
        

    def __init__(self,user,*args,**kwargs):
        super (XarajatForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['user'].queryset =User.objects.filter(id=user)