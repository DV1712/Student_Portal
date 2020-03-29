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
                # auth.login(request,user)
                return render(request, 'Users/log.html')
        else:
            return render(request, 'Users/reg.html', {'error': "Passwords do not match"})
    else:
        return render(request, 'Users/reg.html')

    # userForm = Abs()
    # if request.method = 'POST':
    #
    #     if userForm.is_valid():
    #         email = userForm.cleaned_data['email']
    #         username = userForm.cleaned_data['username']
    #         password = userForm.cleaned_data['password']
    #         dob = userForm.cleaned_data['date_of_birth']
    #         department = userForm.cleaned_data['department']
    #
    #         try:
    #             with transaction.atomic():
    #                 # All the database operations within this block are part of the transaction
    #                 user = User.objects.create_user(email=email, username=username, password=password)
    #                 profile = Profile.objects.create(user=user, date_of_birth=dob, department=department)
    #         except DatabaseError:
    #             # The transaction has failed. Handle appropriately
    #             pass
    # else:
    #     return render(request, 'Users/reg.html')


def login_page(request):
    return render(request, 'Users/log.html')


def home(request):
    return render(request, 'Users/index.html')


# default django registration form template
def register(request):
    pass
    # form = UserCreationForm()
    #
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         return HttpResponse("Hello, Django!")
    #
    # context = {'form': form}
    # return render(request, 'Users/registration.html', context)


def reg_user(request):
    return render(request, 'Users/base.html')

# if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(request, user)
#         return redirect('home')
# else:
#     form = UserCreationForm()
# return render(request, 'signup.html', {'form': form})


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
