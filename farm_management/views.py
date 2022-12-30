from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import FarmInsertForm, barnInsertForm, barnUpdateForm
from django.http import HttpResponse 
from .models import Farm_Management, Barn_Management

# Create your views here.

@login_required(login_url="/users/")
def farm_management_view(request):
    context = {}
    
    load_template = request.path.split('/')
    context['segment'] = load_template

    getUser = get_user_model()
    user = get_object_or_404(getUser, username=request.user)


    return render(request, "farm_management.html", context)

def get_farm_list_up():
    farm_list_up = Farm_Management.objects.all()
    return farm_list_up

def farm_list_up(request):
    # context
    context = {}
    context['farm_list'] = get_farm_list_up()
    
    return render(request, "farm_list.html", context)

def farm_insert_view(request):
    msg = None
    success = False

    context = {}
    if request.method == "POST":
        form = FarmInsertForm(request.POST)
    
        if form.is_valid():
            print("1111111111form1111111")
            new_farm = form.save(commit=False)
            new_farm.insert_id = request.user.username

            print(new_farm.farm_name,
            new_farm.company_num,
            new_farm.farm_owner,
            new_farm.farm_postcode,
            new_farm.farm_addr1,
            new_farm.farm_addr2,
            new_farm.farm_tel_num,
            new_farm.farm_status)
            new_farm.save()

            msg = "등록이 완료되었습니다."
            success = True
            return HttpResponse(status=204, headers={'HX-Trigger':'farmListPageChanged'})
    else:
        form = FarmInsertForm()

    context['form'] = form
    context['msg'] = msg
    context['success'] = success

    return render(request, "farm_insert.html", context)

# barn 등록 view
def get_barn_list_up():
    barn_list_up = Barn_Management.objects.all()
    return barn_list_up

def barn_list_up(request):
    # context
    context = {}
    context['barn_list'] = get_barn_list_up()
    
    return render(request, "barn_list.html", context)

def barn_insert_view(request):
    msg = None
    success = False
    
    context = {}
    if request.method == "POST":
        form = barnInsertForm(request.POST)
    
        if form.is_valid():
            print("1111111111form1111111")
            new_barn = form.save(commit=False)

            print(new_barn.barn_code,
            new_barn.barn_name,
            new_barn.barn_info_scale,
            new_barn.barn_info_volumn,
            new_barn.barn_info_bigo,)
            new_barn.save()

            msg = "등록이 완료되었습니다."
            success = True
            return HttpResponse(status=204, headers={'HX-Trigger':'barnListPageChanged'})
    else:
        form = barnInsertForm()
    
    context['form'] = form
    context['msg'] = msg
    context['success'] = success
    
    return render(request, "barn_insert.html", context)

# barn 수정
def barn_update(request, farm_code):
    error_type = None
    msg = None
    success = False
    context = {}
    
    if len(get_barn_list_up(farm_code)) == 0:
        error_type = 'error01'
        msg = "잘못된 접근입니다."
        barn_data = None
        form=None
    else:
        barn_data = get_barn_list_up(farm_code)[0]

    if request.method == 'POST':
        form = barnUpdateForm(request.POST, instance=barn_data)
        msg = "등록이 완료되었습니다."
        success = True

        if form.is_valid():
            new_commit = form.save(commit=False)
            new_commit.save()

            return HttpResponse(status=204, headers={'HX-Trigger':'barnListChanged'})
    else:
        if barn_data :
            form = barnUpdateForm(instance=barn_data)
        else:
            form = None
    
    context['error_type'] = error_type
    context['msg'] = msg
    context['success'] = success
    context['form'] = form
    context['barn_data'] = barn_data
    
    return render(request, "barn_update.html", context)