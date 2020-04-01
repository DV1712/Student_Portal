from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import *
from Users.models import UserInfo
from Users import models


@login_required()
def show_user(request, sap):
    if sap == "0":
        u = '/profile/' + request.user.username
        datas = UserInfo.objects.filter(user=request.user)
        return redirect(u, {'data': datas})
    else:
        if (request.user.username == sap) or request.user.is_staff:
            datas = UserInfo.objects.filter(user=request.user)
            print(datas)
            return render(request, 'Profile/profile.html', {'data': datas})
        else:
            return HttpResponse('You are not authorized to view this profile!')


@login_required()
def edit_user(request):
    if request.method == 'POST':
        datas = UserInfo.objects.filter(user=request.user)
        user = request.user
        user.email = request.POST['email']
        UserInfo.objects.filter(user_id=request.user.id).update(phone_num=request.POST['phone'],
                                                                languages=request.POST['languages'],
                                                                projects=request.POST['projects'],
                                                                cgpa=request.POST['cgpa'],
                                                                core=request.POST['core'],
                                                                experience=request.POST['experience'])

        user.save()
        return render(request, 'Profile/edit_profile.html', {'data': datas})
    else:
        datas = UserInfo.objects.filter(user=request.user)
        return render(request, 'Profile/edit_profile.html', {'data': datas})


@login_required()
def browse_page(request):
    if request.user.is_staff:
        query_set = UserInfo.objects.all()
        context = {"object_info": query_set}
        return render(request, 'Profile/browse.html', context)
    else:
        return HttpResponse('You are not authorized to view this profile!')


def logout(request):
    auth.logout(request)
    return redirect('/')


def attendance(request):
    return render(request, 'Profile/attendance.html')
