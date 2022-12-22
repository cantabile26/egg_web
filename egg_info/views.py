from django.shortcuts import render

from .forms import Egg_Info_Form

# Create your views here.

def egg_info_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "egg_info.html", context)

# def egg_info_modal(request):
#   if request.method == 'POST':

#     count = Egg_Info_Form(request.POST)
#     count.farm_code = request.POST['farm_code']
#     count.barn_code = request.POST['barn_code']
#     count.egg_registration_date = request.POST['egg_registration_date']
#     count.egg_type = request.POST['egg_type']
#     count.egg_number = request.POST['egg_number']
#     count.save()

    

#     return render(request, 'egg_info.html')

def farm_management_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "farm_management.html", context) 