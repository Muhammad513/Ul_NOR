from django.db import models
import datetime
from django.contrib.auth.models import User
import datetime

class Bank(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.name)


class XarajatTuri(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self) -> str:
        return str(self.name)
    

class Xarajatlar(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    date=models.DateField(blank=True,null=True)
    name=models.ForeignKey('XarajatTuri',on_delete=models.PROTECT)
    summ=models.FloatField()
    manba=models.ForeignKey('Bank',on_delete=models.PROTECT ,null=True)
    comment=models.TextField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)

class Hodim(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    oname=models.CharField(max_length=20)
    jshir=models.CharField(max_length=14)
    pasport=models.CharField(max_length=9)

    def __str__(self) -> str:
        return str(f'{self.fname} {self.lname} {self.oname}')

class IshxaqiXarajati(models.Model):
    date=models.DateField(null=True,blank=True)
    hodim=models.ForeignKey('Hodim',on_delete=models.PROTECT)
    summa=models.FloatField()
    comment=models.TextField()


