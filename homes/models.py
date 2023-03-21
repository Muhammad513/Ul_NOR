from django.db import models
import datetime
from django.contrib.auth.models import User


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
    date=models.DateField()
    name=models.ForeignKey('XarajatTuri',on_delete=models.PROTECT)
    summ=models.FloatField()
    manba=models.ForeignKey('Bank',on_delete=models.PROTECT ,null=True)
    comment=models.TextField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return str(self.name)