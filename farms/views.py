from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from farms.models import Farm, Barn, User_Farm


def get_farm_list(user=None):
  q = Q()
  if user is not None:
    q.add(Q(user_id=user), q.AND)
  farm_list = User_Farm.objects.filter(q)
  
  return farm_list


# 농가관리 main page
@login_required(login_url="/users/")
def farm_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template

  getUser = get_user_model()
  user = get_object_or_404(getUser, username=request.user)
  
  print(user.username)
  print(user)
  print(get_farm_list(user))
  
  return render(request, "farm.html", context)
  
