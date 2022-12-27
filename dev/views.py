from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import CodeUp, CodeDown
from .form import CodeInsertForm, CodeUdateForm

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
def  get_code_down_list(up_code):
  q = Q()
  q.add(Q(code_up_code=up_code), q.AND)
  q.add(Q(code_down_status="show") | Q(code_down_status="hide"), q.AND)
  code_down_list = CodeDown.objects.filter(q)
  print()
  print('get code up list', code_down_list)
  
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
  else:
    code_up_data = get_code_up_list(code_up_code)[0]
    form = CodeUdateForm(request.POST or None, instance=code_up_data)
    print(form)
    if request.method == 'POST':
      msg = "등록이 완료되었습니다."
      success = True
      print('ttt', form.is_valid())
      if form.is_valid():
        print("111111", form)
        new_commit = form.save(commit=False)
        # print(new_commit.code_up_name)
        return HttpResponse(status=204, headers={'HX-Trigger':'codeUpListChanged'})
        
  context['error_type'] = error_type
  context['msg'] = msg
  context['success'] = success
  context['form'] = form
  
  return render(request, "code_up_update.html", context)
  
# 종료 - 상위코드 부분

# 하위코드 부분
def view_code_down_list(request, code_up):
  print('select code', code_up)
  # context
  context = {}
  context['code_down'] = get_code_down_list(code_up)
  context['code_up_code'] = code_up
  
  return render(request, "code_down_list.html", context)