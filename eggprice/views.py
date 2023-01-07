from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from egg.function import api_connect
import datetime
from django.utils import timezone

@login_required(login_url="/users/")
def price_view(request):
  # context
  context = {}
  # path setting
  load_template = request.path.split('/')
  
  context['segment'] = load_template
  context['nav_path'] = {'f':'시세', 's':'계란시세'}
  
  start_date = datetime.datetime.now()-datetime.timedelta(days=7)
  end_date = datetime.datetime.now()
  # 데이터 피커요
  start_date_dp = start_date.strftime("%m/%d/%Y")
  end_date_dp  = end_date.strftime("%m/%d/%Y")
  # parameter 용
  param_sd = start_date.strftime("%Y%m%d")
  param_ed = end_date.strftime("%Y%m%d")
  
  context['start_date'] = start_date_dp
  context['end_date'] = end_date_dp
  
  context['start_date_pr'] = param_sd
  context['end_date_pr'] = param_ed
  
  # print(context)
  
  
  # param={'startYmd':'20220104', 'endYmd':'20220106', 'type':'1', 'numOfRows':'100', 'pageNo':'1'}
  # price_list = api_connect('price', param)
  
  # data = {}
  
  # for item in price_list.find_all('item'):
  
  #   modymd = datetime.datetime.strptime(item.find('modymd').text, '%Y%m%d')
  #   if modymd not in data:
      
  #     data[modymd]={'do':[], 'sa':[]} 
    
  #   if item.typename.text == "도매":
  #     data[modymd]['do'].append('{0:,}'.format(int(item.big.text)))
  #     data[modymd]['do'].append('{0:,}'.format(int(item.medium.text)))
  #     data[modymd]['do'].append('{0:,}'.format(int(item.small.text)))
  #     data[modymd]['do'].append('{0:,}'.format(int(item.special.text)))
  #     data[modymd]['do'].append('{0:,}'.format(int(item.verybig.text)))
      
  #   if item.typename.text == "산지":
  #     data[modymd]['sa'].append('{0:,}'.format(int(item.big.text)))
  #     data[modymd]['sa'].append('{0:,}'.format(int(item.medium.text)))
  #     data[modymd]['sa'].append('{0:,}'.format(int(item.small.text)))
  #     data[modymd]['sa'].append('{0:,}'.format(int(item.special.text)))
  #     data[modymd]['sa'].append('{0:,}'.format(int(item.verybig.text)))
    
    
  # # print(data)  
  # context['prices'] = data
  return render(request, "egg_price.html", context)

def price_data_list(request, start_date, end_date):
  context = {}
  
  param={'startYmd':start_date, 'endYmd':end_date, 'type':'1', 'numOfRows':'100', 'pageNo':'1'}
  price_list = api_connect('price', param)
  
  data = {}
  
  for item in price_list.find_all('item'):
    # print(item)
    modymd = datetime.datetime.strptime(item.find('modymd').text, '%Y%m%d')
    if modymd not in data:
      
      data[modymd]={'do':[], 'sa':[]} 
    
    if item.typename.text == "도매":
      data[modymd]['do'].append('{0:,}'.format(int(item.big.text)))
      data[modymd]['do'].append('{0:,}'.format(int(item.medium.text)))
      data[modymd]['do'].append('{0:,}'.format(int(item.small.text)))
      data[modymd]['do'].append('{0:,}'.format(int(item.special.text)))
      data[modymd]['do'].append('{0:,}'.format(int(item.verybig.text)))
      
    if item.typename.text == "산지":
      data[modymd]['sa'].append('{0:,}'.format(int(item.big.text)))
      data[modymd]['sa'].append('{0:,}'.format(int(item.medium.text)))
      data[modymd]['sa'].append('{0:,}'.format(int(item.small.text)))
      data[modymd]['sa'].append('{0:,}'.format(int(item.special.text)))
      data[modymd]['sa'].append('{0:,}'.format(int(item.verybig.text)))
    
    
  print(data)  
  context['prices'] = data
  
  
  return render(request, "egg_price_list.html", context)