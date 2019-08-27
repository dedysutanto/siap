"""Model Salary"""
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from django.db import models
#from django.db.models.signals import post_save
#from django.dispatch import receiver

# Create your models here.
PAYMENT_FREQUENCY = (
    ("HOUR", "Hour"),
    ("DAY", "Day"),
    ("MONTH", "Month"),
    ("YEAR", "Year"),
)    

class AdditionalSalary(models.Model):
    """Additional Salary"""
   
    class Meta:
        db_table = "additionalsalary"

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='IDR')
    frequency = models.CharField(max_length=10, choices=PAYMENT_FREQUENCY, default="MONTH")

    def __str__(self):
        return "{} - {} - {} - {}".format(self.code, self.name, self.amount, self.frequency)


class Salary(models.Model):
    """Model Salary"""

    class Meta:
        db_table = "salary"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    base = MoneyField(max_digits=14, decimal_places=2, default_currency='IDR')
    additional = models.ManyToManyField(AdditionalSalary)
    
    def __str__(self):
        return "{} - {}".format(self.user, self.base)

