from curses.ascii import US
import json
from operator import imod, truediv
from telnetlib import STATUS
from urllib import request
from django.shortcuts import render
from .models import User
from .models import poinofsale
from .models import Accounts
from .serializer import userSerializer
from .serializer import accountSerializer
from .serializer import posSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['POST'])

def login(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    email = pythondata['email']
    password = pythondata['password']
    try:
        u = User.objects.get(email = email,password=password)
    except :
        content = {'msg', 'not exist'}
        return Response(content,status=status.HTTP_302_FOUND)
    if (request.method == 'POST'):
        serializer = userSerializer(u)
        json_data = JSONRenderer().render(serializer.data)
        return Response({'msg':'user exist'},status=status.HTTP_200_OK)
@api_view(['POST'])
def Createaccount(request):
    if (request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        print(pythondata)
        serializer = accountSerializer(data = pythondata)

        if serializer.is_valid():
            print(serializer.errors)
            serializer.validated_data
            serializer.create(serializer.validated_data)
            res = {"msg","User Create"}
            json_data = JSONRenderer().render(res)
            return Response(json_data,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return  Response({"msg","Some error"},status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def pos(request):
    if (request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = posSerializer(data = pythondata)
        if serializer.is_valid():
            print(serializer.errors)
            serializer.validated_data
            serializer.create(serializer.validated_data)
            res = {"msg","User Create"}
            json_data = JSONRenderer().render(res)
            return Response(json_data,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({"msg", "ERROR"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

def getdatawithaccountnumber(request):
    if (request.method == 'GET'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        accountnumber = pythondata['ACCOUNTNUMBER']
        print(accountnumber)
        try:
            u = poinofsale.objects.get(Accountnumber = accountnumber)
        except:
            content = {'msg', 'not exist'}
            return Response(content, status=status.HTTP_302_FOUND)
        if (request.method == 'GET'):
            serializer =  posSerializer(u)
            json_data = JSONRenderer().render(serializer.data)
            return Response(json_data, status=status.HTTP_200_OK)




