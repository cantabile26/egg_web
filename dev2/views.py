from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse 
from django.db.models import Q
from users.models import User
from .form import BoardForm
from django.core.paginator import Paginator  
from django.views.decorators.csrf import csrf_exempt


#수정페이지
def aaa(request, id):
    update = User.objects.get(id=id)
    print(request.method)
    if request.method =='POST':
      form = BoardForm(request.POST)
      if form.is_valid():
        update.nickname = form.cleaned_data['nickname']
        update.user_type = form.cleaned_data['user_type']
        update.user_status = form.cleaned_data['user_status']
        update.save()
        return HttpResponse(status=204, headers={'HX-Trigger':'userListChanged'})#HttpResponseRedirect('/dev2/usermanage/') 
    else:
      form = BoardForm(instance = update)
      print("trsttttttt")
      return render(request,'aaa.html', {'form':form})



@csrf_exempt
def view_uuser_list(request):
  # context
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  uuser = User.objects.all()
  context = {'uuser':uuser }

  return render(request, "uuser_up_list.html", context)


def user_manage(request):
  # context
  context = {}
  # path setting
  load_template = request.path.split('/')
  
  context['segment'] = load_template
#   context['code_down'] = False;
  
  getUser = get_user_model()
  user = get_object_or_404(getUser, username=request.user)
  

  
  return render(request, "user_list_zore.html", context)



#AttributeError: 'QuerySet' object has no attribute '_meta'




