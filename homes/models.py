from django.db import models
import datetime
class XarajatTuri(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self) -> str:
        return str(self.name)
    

class Xarajatlar(models.Model):
    date=models.DateField(auto_now=datetime)
    name=models.ForeignKey('XarajatTuri',on_delete=models.PROTECT)
    summ=models.FloatField()
