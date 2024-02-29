from http.client import responses
from ssl import _PasswordType
from urllib import response
from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_viewi , permission_classes,actions
from rest_framework.permissions import AllowAny

def creat_user(req):
    first_name = req.POST["first_name"]
    last_name = req.POST["last_name"]
    password = req.POST["password"]
    
    user = IMUser.objects.create(first_name=first_name, last_name = last_name)
    user.set_password(password)
    user.save()
    return "User created"

def _str_(self):




@api_view(['post'])
@permission_classes([AllowAny])
def signup (request):
    username= request.data.get("username")
    firstname= request.data.get("first_name?")
    last_name=last_name.data.get("last_name")

    new_user= IMUser.objects.created(
        username=username,
        first_name=first_name,
        last_name=last_name,
    )
    new_user.set_password(_PasswordType)
    new_user.save()
    new_user.generate_auth_token()
    userSerializer=userSerializer(new_user, many=False)
    return response({"message": "Account successfully created", "result":userSerializer.data})
#login

@api_viewi(['POST'])
@permission_classes([AllowAny]) 
def login(request):
    #recieve input data from client and validate inputs
    username = request.data.get("username")
    password= request.data.get("password")
    if not username or not password:
        return responses (["detail": "My friend, will you send the username"])





