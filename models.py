from django.db import models

# Create your models here.
class User(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=40)

class Accounts(models.Model):
    Name = models.CharField(max_length=100)
    Account = models.IntegerField()
    Phone_no = models.IntegerField()
    Idcardno = models.IntegerField()
    Address = models.CharField(max_length=100)
    Debt = models.IntegerField()
class poinofsale(models.Model):
    Date = models.DateField()
    Accountnumber = models.IntegerField()
    Customername = models.CharField(max_length=100)
    Productname = models.CharField(max_length=100)
    Price = models.IntegerField()
    Downpayment = models.IntegerField()
    Totalinstallment = models.IntegerField()
    Perinstallment = models.IntegerField()
    Total = models.IntegerField()
    Paid = models.IntegerField()
    Remaininginstallment = models.IntegerField()