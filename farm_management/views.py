from django.shortcuts import render

# Create your views here.

def farm_management_view(request):
    context = {}
    
    load_template = request.path.split('/')
    context['segment'] = load_template

    return render(request, "farm_management.html", context)

def farm_list_view(request):
    context = {}
    
    load_template = request.path.split('/')
    context['segment'] = load_template
    
    return render(request, "farm_list.html", context)

def farm_register_view(request):
    context = {}
    
    load_template = request.path.split('/')
    context['segment'] = load_template
    
    return render(request, "farm_register.html", context)