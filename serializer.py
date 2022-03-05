from rest_framework import serializers
from .models import User
from .models import Accounts
from .models import poinofsale
class userSerializer(serializers.Serializer):
    fullName = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=40)

class accountSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=100)
    Account = serializers.IntegerField()
    Phone_no = serializers.IntegerField()
    Idcardno  = serializers.IntegerField()
    Address = serializers.CharField(max_length=100)
    Debt = serializers.IntegerField()

    def create(self,validate_data):
        return Accounts.objects.create(**validate_data)
class posSerializer(serializers.Serializer):
    Date = serializers.DateField()
    Accountnumber = serializers.IntegerField()
    Customername = serializers.CharField(max_length=100)
    Productname = serializers.CharField(max_length=100)
    Price = serializers.IntegerField()
    Downpayment = serializers.IntegerField()
    Totalinstallment = serializers.IntegerField()
    Perinstallment = serializers.IntegerField()
    Total = serializers.IntegerField()
    Paid = serializers.IntegerField()
    Remaininginstallment = serializers.IntegerField()
    def create(self, validated_data):
        return poinofsale.objects.create(**validated_data)
