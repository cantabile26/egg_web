from django.shortcuts import render
from users.models import User
from django.contrib.auth import authenticate, login, logout
from egg.function import s2j1c1_encrypt, s2j1c1_decrypt 
from .forms import LoginForm, SignUpForm
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.urls import reverse

# 로그인
def login_view(request):
  form = LoginForm(request.POST or None)
  msg = None
  
  context = {}
  if request.method == "POST":
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      en_username = s2j1c1_encrypt(username)
      
      user = authenticate(request, username=en_username, password=password)
      print(user)
      if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('main:mainPage'))
      else:
        msg = "다시 시도해주세요."
    else:
      msg = "잘못된 접근입니다."
  
  context['form'] = form
  context['msg'] = msg
  
  return render(request, "login.html", context)

# 회원가입
def user_register(request):
  msg = None
  success = False
  
  context = {}
  
  if request.user.is_authenticated:
    return render(request, "login.html", context)
  
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      username      = form.cleaned_data.get("username") 
      en_username   = s2j1c1_encrypt(username)
      
      post = form.save(commit=False)
      post.username = en_username
      post.user_type = "farm"
      post.user_status = "1"
      post.insert_id = en_username
      post.insert_date = timezone.localtime()
      
      # insert db
      post.save()
      
      msg = "회원가입이 완료되었습니다."
      success=True
    else:
      msg = "올바른 접근이 아닙니다."
  else:
    form = SignUpForm()
  
  context['form'] = form
  context['msg'] = msg
  context['success'] = success
  
  return render(request, "sign_up.html", context)

# 로그아웃
def logoutAction(request):
  logout(request)
  return HttpResponseRedirect(reverse('users:loginPage'))