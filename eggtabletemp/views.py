from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Accounting

def bootstrapTables(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "bootstrap-tables.html", context)

def eggdetectTables(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "eggdetect-tables.html", context)


def eggmanageTables(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template
  accounting = Accounting.objects.all()
  context = {'account_ing':accounting}
  
  return render(request, 'eggmanage-table.html', context)
  


def eggmanageinputTables(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "input_account.html", context)

def home(request):
    return render(request, 'input_account.html')

def createform(request):

    if request.method == 'POST':
        acc = Accounting()
        acc.farm_code = request.POST['farm_code']
        acc.barn_code = request.POST['barn_code']
        acc.회계코드 = request.POST['회계코드']
        acc.계좌번호 = request.POST['계좌번호']
        acc.출납일 = request.POST['출납일']
        acc.발의일 = request.POST['발의일']
        acc.결제일 = request.POST['결제일']
        acc.등기일 = request.POST['등기일']
        acc.결의구분 = request.POST['결의구분']
        acc.계정과목 = request.POST['계정과목']
        acc.적요 = request.POST['적요']
        acc.수입 = request.POST['수입']
        acc.지출 = request.POST['지출']
        acc.자금원천 = request.POST['자금원천']
        acc.정렬 = request.POST['정렬']
        acc.비고 = request.POST['비고']
        acc.save()

    return render(request, 'input_account.html')


def index(request):
    accounting = Accounting.objects.all()
    context = {'account_ing':accounting}
        #context에 모든 db 정보를 저장
    return render(request, 'templates/eggmanage-table.html', context)
        #context안에 있는 db 정보를 index.html로 전달
