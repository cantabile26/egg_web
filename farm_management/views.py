from django.shortcuts import render
from .forms import FarmInsertForm, barnInsertForm
from django.http import HttpResponse 

# Create your views here.

def farm_management_view(request):
    context = {}
    
    load_template = request.path.split('/')
    context['segment'] = load_template

    return render(request, "farm_management.html", context)


def farm_insert_view(request):
    msg = None
    success = False

    context = {}
    if request.method == "POST":
        form = FarmInsertForm(request.POST)
    
        if form.is_valid():
            print("1111111111form1111111")
            new_farm = form.save(commit=False)

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
    else:
        form = FarmInsertForm()

    context['form'] = form
    context['msg'] = msg
    context['success'] = success

    return render(request, "farm_insert.html", context)

# barn 등록 view
def barn_list(request):
    # context
    context = {}
    context['barn_list'] = farm_management_view()
    
    return render(request, "barn_list.html", context)

def barn_insert_view(request):
    msg = None
    success = False
    
    context = {}
    if request.method == "POST":
        form = barnInsertForm(request.POST)
    
        if form.is_valid():
            print("1111111111form1111111")
            form.save(commit=False)

        msg = "등록이 완료되었습니다."
        success = True
        return HttpResponse(status=204, headers={'HX-Trigger':'barnListPageChanged'})
    else:
        form = barnInsertForm()
    
    context['form'] = form
    context['msg'] = msg
    context['success'] = success
    
    return render(request, "barn_insert.html", context)