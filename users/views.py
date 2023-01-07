from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from egg.function import s2j1c1_encrypt, s2j1c1_decrypt,  code_down_value
from .forms import LoginForm, SignUpForm, UserForm
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.urls import reverse

from farms.models import User_Farm
from users.models import User
from dev.models import CodeDown
from django.db.models import Q

def get_user_list():
  q = Q()
  q.add(Q(user_status='1') | Q(user_status='2'), q.AND)
  
  user_list = User.objects.filter(q)
  return user_list



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
      
      if user is not None:
        if user.user_status == '1':
          login(request, user)
          try:
            user_farm = User_Farm.objects.get(user_id=user)
          except User_Farm.DoesNotExist:
            user_farm = None
            
          if user_farm is not None:
            request.session['farm_code'] = user_farm.farm_farm_code.farm_code
          return HttpResponseRedirect(reverse('main:mainPage'))
        else :
          msg = "접근이 불가합니다."
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

# 사용자 list - 관리자용
@login_required(login_url="/users/")
def users_list_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['nav_path'] = {'f':'사용자', 's':'사용자관리'}
  context['segment'] = load_template
  
  return render(request, 'user_list.html', context)

def users_list(request):
  context = {}
  
  user_list = get_user_list()
  print(user_list)
  
  for user in user_list:
    user.user_status_text = code_down_value(1, user.user_status).code_value1
    type_text = '대표자' if user.user_type == 'farm' else '관리자'
    user.user_type_text = type_text
    user.de_username = s2j1c1_decrypt(user.username)
    
  context['users'] = user_list
  
  return render(request, "user_list_data.html", context)

def user_update_view(request, user_code):
  error_type = None
  msg = None
  success = False
  form = None
  context = {}
  
  getUser = get_user_model()
  user = get_object_or_404(getUser, id=user_code)
  if request.method == "POST":
    form = UserForm(request.POST, instance=user)
    
    if form.is_valid():
      new_commit = form.save(commit=False)
      if form.cleaned_data.get("user_password_change"):
        new_commit.set_password(form.cleaned_data.get("user_password_change")) 
        
      new_commit.update_id = request.user.username
      new_commit.update_date = timezone.localtime()
      new_commit.save()
      
      return HttpResponse(status=204, headers={'HX-Trigger':'userListChanged'})
  else:
    form = UserForm(instance=user)
  
  user.de_username = s2j1c1_decrypt(user.username)
  user_status_data = code_down_value(up=1)
  for us in user_status_data:
    us.code_down_text = str(us.code_down)
  context['user_status'] = user_status_data
  
  context['form'] = form
  context['user'] = user
  
  return render(request, "user_update.html", context)