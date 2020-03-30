# import re
# from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http.response import *
from django.db import transaction, DatabaseError

from .models import UserInfo


def registration_page(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['repeatpass']:
            try:
                user = User.objects.get(username=request.POST['sap_id'])
                return render(request, 'Users/reg.html', {'error': "User Already exists with this SAP ID"})
            except User.DoesNotExist:
                user = User.objects.create_user(first_name=request.POST['fname'], last_name=request.POST['lname'],
                                                username=request.POST['sap_id'], email=request.POST['email'],
                                                password=request.POST['pass'])
                stream = request.POST['stream']
                print(stream)
                program = request.POST['program']
                userinfo = UserInfo(stream=stream, program=program, user=user)
                userinfo.save()
                auth.login(request, user)
                return render(request, 'Users/index.html')
        else:
            return render(request, 'Users/reg.html', {'error': "Passwords do not match"})
    else:
        return render(request, 'Users/reg.html')


def login_page(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['sap_id'], password=request.POST['pass'])
        if user is None:
            return render(request, 'Users/log.html', {'error': "SAP ID or Password incorrect!"})
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'Users/log.html')


def home(request):
    return render(request, 'Users/index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

#               AISE HI KCH BHI TRY KRA THA
# def hello_there(request):
#     match_object = re.match("[a-zA-Z]+")
#
#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"
#
#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)
