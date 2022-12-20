from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import CodeUp, CodeDown
from .form import CodeInsertForm


def get_code_up_list():
  result = []
  code_up_list = CodeUp.objects.filter(
    Q(code_up_status="show") | Q(code_up_status="hide")
  )
  
  print('get code up list', len(code_up_list))
  return code_up_list
  
def  get_code_down_list(up_code):
  q = Q()
  q.add(Q(code_up_code=up_code), q.AND)
  q.add(Q(code_down_status="show") | Q(code_down_status="hide"), q.AND)
  code_down_list = CodeDown.objects.filter(q)
  
  print('get code up list', code_down_list)
  
  return code_down_list


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
  # print(getUser)
  # print(request.user)
  context['code_up'] = get_code_up_list()
  # get_code_down_list(1)
  
  return render(request, "code_list.html", context)


def code_up_add(request):
  msg = None
  success = False
  
  context = {}
  if request.method == "POST":
    form = CodeInsertForm(request.POST)
    
    if form.is_valid():
      print("1111111111form1111111")
      print(request.user)
      new_comment = form.save(commit=False)
      new_comment.insert_id = request.user.username
      
      print(new_comment.code_up,
      new_comment.code_up_name,
      new_comment.code_up_info,
      new_comment.code_up_status,
      new_comment.insert_id,
      new_comment.insert_date)
      new_comment.save()
      
      msg = "등록이 완료되었습니다."
      success = True
      return HttpResponse(status=204)
  else:
    form = CodeInsertForm()
  
  context['form'] = form
  context['msg'] = msg
  context['success'] = success
  
  return render(request, "code_up_insert.html", context)


def add_movie(request):
    if request.method == "POST":
        form = CodeInsertForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)
    else:
        form = CodeInsertForm()
    return render(request, 'movie_form.html', {
        'form': form,
    })