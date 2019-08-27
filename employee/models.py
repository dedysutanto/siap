"""Employee Models"""
from django.contrib.auth.models import User
from company.models import Company
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Employee(models.Model):
    """Employee Model"""

    class Meta:
        """Define table name"""
        db_table = "employee"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bod = models.DateField(null=True, blank=True)
    code = models.CharField(max_length=20, blank=False)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.code)


@receiver(post_save, sender=User)
def create_user_employee(sender, instance, created, **kwargs):
    """Auto create employee when new user is added"""
    if created:
        Employee.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_employee(sender, instance, created, **kwargs):
    """Auto save employee"""
    instance.employee.save()
