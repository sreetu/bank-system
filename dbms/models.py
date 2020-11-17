from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    name = models.CharField(max_length=264, default=None)
    email= models.EmailField(default=None)
    balance= models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)

class History(models.Model):
    sender = models.ForeignKey(CustomerDetails, on_delete=models.DO_NOTHING)
    reciever = models.ForeignKey(CustomerDetails, related_name='reciever' , on_delete=models.DO_NOTHING)
    amount = models.FloatField(default=0)
    msg = models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.msg