from django.utils import timezone
from django.shortcuts import render


from .models import Egginfo
from .forms import Egg_Info_Form

# Create your views here.

def egg_info_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "egg_info.html", context)

def egg_data_upload_view(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "egg_data_upload.html", context)


def egg_info_input_modal(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "egg_info.html", context)

def index(request):
  egg_modal_input = Egginfo.objects.all()
  context = {'egg_modal_input':egg_modal_input}
        #context에 모든 db 정보를 저장
  return render(request, 'egg_info.html', context)

def createform(request):

    if request.method == 'POST':
        count = Egg_Info_Form()
        count.farm_code = request.POST['farm_code']
        count.barn_code = request.POST['barn_code']
        count.egg_registration_date = request.POST['egg_registration_date']
        count.egg_type = request.POST['egg_type']
        count.egg_number = request.POST['egg_number']

        count.save()

    return render(request, 'egg_info.html')