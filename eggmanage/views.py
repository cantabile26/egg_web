from django.shortcuts import redirect, render
from .models import Accounting
from django.core.paginator import Paginator  
from django.db.models import Q
from .form import BoardForm
from django.http import HttpResponseRedirect


def eggmanageTables(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template
  accounting = Accounting.objects.all()

  page = request.GET.get('page', '1')  # 페이지
  kw = request.GET.get('kw', '')  # 검색어

  if kw:
      accounting = accounting.filter(
          Q(farm_code=kw) |  # 제목 검색
          # Q(content__icontains=kw) |  # 내용 검색
          Q(barn_code=kw) |  # 답변 내용 검색
          Q(회계코드=kw) |  # 질문 글쓴이 검색
          Q(계좌번호=kw)  # 답변 글쓴이 검색
      ).distinct()
  paginator = Paginator(accounting, 10)  # 페이지당 10개씩 보여주기
  page_obj = paginator.get_page(page)

  context = {'account_ing':accounting, 'accounting': page_obj, 'page': page, 'kw': kw}
  
  return render(request, 'eggmanage-table.html', context)


def eggmanageinputTables(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "input_account.html", context)


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

'''
def update_account(request,회계코드):
  update = Accounting.objects.get(pk=회계코드)
  print(request.method)
  if request.method =='POST':
    form = BoardForm(request.POST)
    if form.is_valid():
      update.farm_code = form.cleaned_data['farm_code']
      update.barn_code = form.cleaned_data['barn_code']
      update.회계코드 = form.cleaned_data['회계코드']
      update.계좌번호 = form.cleaned_data['계좌번호']
      update.출납일 = form.cleaned_data['출납일']
      update.발의일 = form.cleaned_data['발의일']
      update.save()
      return HttpResponseRedirect('/eggmanage-tables/') 
  else:
    form = BoardForm(instance = update)
    print("trsttttttt")
    return render(request,'update_account.html', {'form':form})
'''
