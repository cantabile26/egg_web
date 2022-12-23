from django.shortcuts import render
from .forms import FarmRegisterForm

# Create your views here.

def farm_management_view(request):
    context = {}
    
    load_template = request.path.split('/')
    context['segment'] = load_template

    return render(request, "farm_management.html", context)

def farm_register_view(request):
    msg = None
    success = False

    context = {}

    if request.method == "POST":
        form = FarmRegisterForm(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)

            print(
            post.farm_name,
            post.company_num,
            post.farm_owner,
            post.farm_postcode,
            post.farm_addr1,
            post.farm_addr2,
            post.farm_tel_num,
            post.farm_status)

            msg = "등록이 완료되었습니다."
            success = True
    else:
        form = FarmRegisterForm()

    context['form'] = form
    context['msg'] = msg
    context['success'] = success

    return render(request, "farm_register.html", context)