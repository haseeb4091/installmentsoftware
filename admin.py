
# Register your models here.
from django.contrib import admin
from .models import User
from.models import  Accounts
from .models import poinofsale
# Register your models here.
@admin.register(User)
class userAdmin(admin.ModelAdmin):
    listDisplay = ['id','fullName','age','Email']
@admin.register(Accounts)
class accountAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Account','Phone_no','Idcardno','Address','Debt']

@admin.register(poinofsale)

class posAdmin (admin.ModelAdmin):
    list_display = ['id','Date','Accountnumber','Customername','Productname','Price','Downpayment','Totalinstallment','Perinstallment','Total','Paid','Remaininginstallment']