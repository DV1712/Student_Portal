import re
from django.shortcuts import render,redirect


def reg_user(request):
    return render(request, 'Profile/profile.html')


def edit_user(request):
    return render(request, 'Profile/edit_profile.html')

    # match_object = re1.match("[a-zA-Z]+")
    #
    # if match_object:
    #     clean_name = match_object.group(0)
    # else:
    #     clean_name = "Friend"
    #
    # content = "Hello there, " + clean_name
