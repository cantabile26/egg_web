from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/")
def view_egg_model(request):
  # context
  context = {}
  # path setting
  load_template = request.path.split('/')
  
  context['segment'] = load_template
  context['nav_path'] = {'f':'분류', 's':'계란선별기'}
  
  return render(request, "eggdetect.html", context)

# Create your views here.
