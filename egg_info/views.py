from django.shortcuts import render
from django.http import HttpResponse
 
from .models import Egginfo

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

from django.shortcuts import render

 
# Create your views here.
def Egg_modal_data(request):
    egg_modal_input = Egginfo.objects.all()
    context = {'egg_modal_input':egg_modal_input}
        #context에 모달에서 들어온 데이터를 저장
    return render(request, 'egg_info.html', context)
        #context안에 있는 모달 데이터를 egg_info.html로 전달