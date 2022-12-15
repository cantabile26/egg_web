from django.shortcuts import render

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