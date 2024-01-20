from django.db import models

# Create your models here.
class Department(models.Model):
    """Department"""
    title = models.CharField(verbose_name="title", max_length=16)

    def __str__(self):
        return self.title

class Admin(models.Model):
    """Employee"""
    username = models.CharField(verbose_name="username", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)
    age = models.IntegerField(verbose_name="age", null=True, blank=True)
    gender = models.IntegerField(
        verbose_name="gender", 
        choices=[(1,"Male"), (2,"Female")],
        default=1
        )
    depart =models.ForeignKey(verbose_name="department", to="Department", on_delete=models.CASCADE)

class Phone(models.Model):
    """Phone Number"""
    mobile = models.CharField(verbose_name="phone number", max_length=11)
    price = models.PositiveIntegerField(verbose_name="price", default=0)
    level = models.SmallIntegerField(
        verbose_name="level",
        choices=[(1,"level 1"),(2, "level 2"),(3, "level 3"),(4, "level 4")],
        default=1
    )
    status = models.SmallIntegerField(
        verbose_name="status",
        choices=[(1,"Used"),(2,"Not used")],
        default=2
    )