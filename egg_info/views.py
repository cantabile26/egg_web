from django.shortcuts import render

from .forms import Egg_Info_Form

# Create your views here.

def egg_info_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "egg_info.html", context)