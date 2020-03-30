from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http.response import *
from Users.models import UserInfo


@login_required()
def show_user(request, sap):
    if sap == "0":
        u = '/profile/' + request.user.username
        return redirect(u)
    else:
        if (request.user.username == sap) or request.user.is_staff:
            return render(request, 'Profile/profile.html')
        else:
            return HttpResponse('You are not authorized to view this profile!')


@login_required()
def edit_user(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        UserInfo.objects.filter(user_id=request.user.id).update(phone_num=request.POST['phone'])
        user.save()
        return render(request, 'Profile/edit_profile.html')
    else:
        return render(request, 'Profile/edit_profile.html')


@login_required()
def browse_page(request):
    if (request.user.is_staff):
        return render(request, 'Profile/browse.html')
    else:
        return HttpResponse('You are not authorized to view this profile!')


def logout(request):
    auth.logout(request)
    return redirect('/')
