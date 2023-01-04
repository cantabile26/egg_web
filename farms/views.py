from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from farms.models import Farm, Barn, User_Farm
from farms.forms import FarmListForm, FarmInsertForm, FarmUpdateForm
from egg.function import s2j1c1_encrypt

def get_user_farm_list(user=None):
  q = Q()
  if user is not None:
    q.add(Q(user_id=user), q.AND)
  farm_user_list = User_Farm.objects.filter(q)
  
  return farm_user_list

def get_farm_list(farm_code=None):
  q = Q()
  if farm_code is not None:
    q.add(Q(farm_code=farm_code), q.AND)
    q.add(Q(farm_status="show"), q.AND)
  farm_list = Farm.objects.filter(q)
  
  return farm_list

# farm 관련 - 시작
# 농가관리 main page
@login_required(login_url="/users/")
def farm_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "farm.html", context)

# 농가관리 main view
def farm_list_view(request):
  context = {}
  getUser = get_user_model()
  user = get_object_or_404(getUser, username=request.user)
  
  if len(get_user_farm_list(user)) > 0:
    farm_user = get_user_farm_list(user)[0]
    farm_list = get_farm_list(farm_user.farm_farm_code.farm_code)[0]
  else:
    farm_user = None
    farm_list = None
  form = FarmListForm(instance=farm_list)
  
  context['farm_user'] = farm_user
  context['form'] = form
  
  return render(request, "farm_list.html", context)

# farm insert view
def farm_insert_view(request):
  msg = None
  success = False
  
  context = {}
  if request.method == "POST":
    form = FarmInsertForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
      commit = form.save(commit=False)
      commit.insert_id = request.user.username
      # farm code making
      farm_list_len = len(get_farm_list())
      farm_code_res = "a"+str(farm_list_len+1).zfill(10)
      commit.farm_code = s2j1c1_encrypt(farm_code_res)
      # farm save
      commit.save()
      # farm_user save
      farmdata = get_farm_list(s2j1c1_encrypt(farm_code_res))[0]
      getUser = get_user_model()
      user = get_object_or_404(getUser, username=request.user)
      uer_farm = User_Farm()
      uer_farm.user_id = user
      uer_farm.farm_farm_code = farmdata
      
      uer_farm.save()
      
      return HttpResponse(status=204, headers={'HX-Trigger':'farmListChange'})
  else:
    form = FarmInsertForm()
  
  context['form'] = form
  context['msg'] = msg
  context['success'] = success
    
  return render(request, 'farm_insert.html', context)

#farm update view 
def farm_update_view(request, farm_code):
  context = {}
  farm_data = get_farm_list(farm_code)[0]
  print(farm_data)
  
  error_type = None
  msg = None
  success = False
  context = {}
  
  if len(get_farm_list(farm_code)) == 0:
    error_type = 'error01'
    msg = "잘못된 접근입니다."
    farm_data = None
    form=None
  else:
    farm_data = get_farm_list(farm_code)[0]
    
  if request.method == 'POST':
    form = FarmUpdateForm(request.POST, instance=farm_data)
    msg = "수정이 완료되었습니다."
    success = True
    
    if form.is_valid():
      new_commit = form.save(commit=False)
      new_commit.update_id = request.user.username
      new_commit.save()
      
      return HttpResponse(status=204, headers={'HX-Trigger':'farmListChange'})
  else:
    if farm_data :
      form = FarmUpdateForm(instance=farm_data)
    else:
      form = None
  
  context['error_type'] = error_type
  context['msg'] = msg
  context['success'] = success
  context['form'] = form
  context['farm_data'] = farm_data
  
  return render(request, 'farm_update.html', context)

# 종료 - farm 관련 

# barn관련