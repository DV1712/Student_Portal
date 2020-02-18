# import re
# from datetime import datetime

from django.shortcuts import render


def registration_page(request):
    return render(request, 'Users/register.html')


def login_page(request):
    return render(request, 'Users/login.html')


def home(request):
    return render(request, 'Users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#               AISE HI KCH BHI TRY KRA THA
#
# def home(request):
#     return HttpResponse("Hello, Django!")
#
#
# def hello_there(request):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")
#
#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+")
#
#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"
#
#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)




