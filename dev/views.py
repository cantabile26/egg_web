from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import CodeUp, CodeDown
from .form import CodeInsertForm, CodeUdateForm, CodeDownInsertForm, CodeDownUpdateForm

# 모델 부분
# 코드업 리스트! - 가져오기 to db
def get_code_up_list(code_up_code=0):
  result = []
  q = Q()
  q.add(Q(code_up_status="show") | Q(code_up_status="hide"), q.AND)
  if code_up_code != 0:
    q.add(Q(code_up=code_up_code), q.AND)
  
  code_up_list = CodeUp.objects.filter(q)
  
  return code_up_list


# 코드 다운 리스트 - 가져오기 to db
def  get_code_down_list(up_code, code_down_code=0):
  q = Q()
  q.add(Q(code_up_code=up_code), q.AND)
  if code_down_code != 0:
    q.add(Q(code_down=code_down_code), q.AND)
  q.add(Q(code_down_status="show") | Q(code_down_status="hide"), q.AND)
  code_down_list = CodeDown.objects.filter(q)
  
  return code_down_list
# 종료 - 모델 부분 

@login_required(login_url="/users/")
def code_view(request):
  # context
  context = {}
  # path setting
  load_template = request.path.split('/')
  
  context['segment'] = load_template
  context['code_down'] = False;
  
  getUser = get_user_model()
  user = get_object_or_404(getUser, username=request.user)
  
  context['code_up'] = get_code_up_list()
  
  return render(request, "code_list.html", context)

# 시작 -- 상위코드 부분  
def view_code_up_list(request):
  # context
  context = {}
  context['code_up'] = get_code_up_list()
  
  return render(request, "code_up_list.html", context)
# 상위코드 추가
def code_up_add(request):
  msg = None
  success = False
  
  context = {}
  if request.method == "POST":
    form = CodeInsertForm(request.POST)
    
    if form.is_valid():
      new_commit = form.save(commit=False)
      new_commit.insert_id = request.user.username
      
      print(new_commit.code_up,
      new_commit.code_up_name,
      new_commit.code_up_info,
      new_commit.code_up_status,
      new_commit.insert_id,
      new_commit.insert_date)
      new_commit.save()
      
      msg = "등록이 완료되었습니다."
      success = True
      return HttpResponse(status=204, headers={'HX-Trigger':'codeUpListChanged'})
  else:
    form = CodeInsertForm()
  
  context['form'] = form
  context['msg'] = msg
  context['success'] = success
  
  return render(request, "code_up_insert.html", context)

# 상위코드 수정
def code_up_update(request, code_up_code):
  error_type = None
  msg = None
  success = False
  context = {}
  
  if len(get_code_up_list(code_up_code)) == 0:
    error_type = 'error01'
    msg = "잘못된 접근입니다."
    code_up_data = None
    form=None
  else:
    code_up_data = get_code_up_list(code_up_code)[0]
    
  if request.method == 'POST':
    form = CodeUdateForm(request.POST, instance=code_up_data)
    msg = "등록이 완료되었습니다."
    success = True
    
    if form.is_valid():
      new_commit = form.save(commit=False)
      new_commit.update_id = request.user.username
      new_commit.save()
      
      return HttpResponse(status=204, headers={'HX-Trigger':'codeUpListChanged'})
  else:
    if code_up_data :
      form = CodeUdateForm(instance=code_up_data)
    else:
      form = None
  
  context['error_type'] = error_type
  context['msg'] = msg
  context['success'] = success
  context['form'] = form
  context['code_up_data'] = code_up_data
  
  return render(request, "code_up_update.html", context)

# 상위코드 삭제 
def code_up_delete(request, code_up_code):  
  code_up = CodeUp.objects.get(code_up=code_up_code)  
  code_up.delete()
  
  return HttpResponse(status=204, headers={'HX-Trigger':'codeListChanged'})
# 종료 - 상위코드 부분

# 시작 - 하위코드 부분
def view_code_down_list(request, code_up):
  print('request', request.path)
  print('select code', code_up)
  none_msg = '좌측의 상위코드를 선택해 주세요.' if code_up == 0 else '등록된 내용이 없습니다.'
  code_up_data = get_code_up_list(code_up)[0] if code_up != 0 else ''
  
  # context
  context = {}
  context['code_down'] = get_code_down_list(code_up)
  context['code_up_data'] = code_up_data
  context['code_up'] = code_up if code_up else 0
  context['none_msg'] = none_msg
  
  return render(request, "code_down_list.html", context)

# code down insert
def code_down_add(request, code_up_code):
  print(CodeUp.objects.get(code_up=code_up_code))
  msg = None
  success = False
  
  context = {}
  code_up_data = CodeUp.objects.get(code_up=code_up_code)
  if request.method == "POST":
    form = CodeDownInsertForm(request.POST)
    if form.is_valid():
      new_commit = form.save(commit=False)
      
      new_commit.code_up_code = code_up_data
      new_commit.insert_id = request.user.username
      
      new_commit.save()
      
      msg = "등록이 완료되었습니다."
      success = True
      
      return HttpResponse(status=204, headers={'HX-Trigger':'codeDownListChanged'})
  else:
    form = CodeDownInsertForm()
  
  context['form'] = form
  context['code_up_code'] = code_up_data
  context['msg'] = msg
  context['success'] = success
  
  return render(request, "code_down_insert.html", context) 

#code down update
def code_down_update(request, code_up_code, code_down_code):
  print(code_up_code)
  print(code_down_code)
  error_type = None
  msg = None
  success = False
  form = None
  context = {}
  
  if len(get_code_down_list(code_up_code, code_down_code)) == 0:
    error_type = 'error01'
    msg = "잘못된 접근입니다."
    code_down_data = None
  else:
    code_down_data = get_code_down_list(code_up_code, code_down_code)[0]
    
  if request.method == 'POST':
    form = CodeDownUpdateForm(request.POST, instance=code_down_data)
    msg = "등록이 완료되었습니다."
    success = True
    
    if form.is_valid():
      new_commit = form.save(commit=False)
      new_commit.update_id = request.user.username
      new_commit.save()
      
      return HttpResponse(status=204, headers={'HX-Trigger':'codeDownListChanged'})
  else:
    if code_down_data :
      form = CodeDownUpdateForm(instance=code_down_data)
    
  
  context['error_type'] = error_type
  context['msg'] = msg
  context['success'] = success
  context['form'] = form
  context['code_up_code'] = code_up_code
  context['code_down_data'] = code_down_data
  
  return render(request, "code_down_update.html", context)

# 하위코드 삭제 
def code_down_delete(request, code_up_code, code_down_code):  
  print(code_up_code, code_down_code)
  code_down_data = get_code_down_list(code_up_code, code_down_code)[0]
  code_down_data.delete()
  
  return HttpResponse(status=204, headers={'HX-Trigger':'codeDownListChanged'})
# 종료 - 하위코드 부분