from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

'''
def sign_in_table(request):
  print(request)
    if request.user.is_authenticated:
        return render(request, "sign-in.html")
    if request.method == "POST":
        print(request.POST)
        email = request.POST['email']
        passwrd = request.POST['passwrd']
        passwrd_chk = request.POST['passwrd_chk']
        user = User.objects.filter(username=email)
        if len(user) > 0:
            context = {'form': request.POST, 'error':'id'}
            return render(request, "sign-up.html", context)
        if passwrd == passwrd_chk:
            User.objects.create_user(
                password = passwrd,
                email = email,
            )
            return HttpResponseRedirect(reverse('users:sign_in_tablePage'))
        else:
            context = {'form': request.POST}
            return render(request, "sign-up.html", context)

    return render(request, "sign-up.html")

'''


def sign_in_table(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "sign-in.html", context)



def sign_up_table(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "sign-up.html", context)
