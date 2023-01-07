import os
import base64
from django.db.models import Q
from dev.models import CodeDown
from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup


# 암호화
def s2j1c1_encrypt(value):
  key = os.getenv('PASSING_KEY', '3askdj1i2o3uq7sd8axzhqurhajsdhyg1238asdzjxcyew5ras')
  
  result = ""
  str_value = str(value)
  for i in range(len(str_value)):
    val1 = ord(str_value[i])+len(str_value)
    key1 = ord(key[i%len(str_value)])
    val_res = val1^key1
    
    result = result+chr(val_res)
    
  result_bytes = result.encode('ascii')
  result_base64 = base64.b64encode(result_bytes)
  result_base64_str = result_base64.decode('ascii') 
  
  return result_base64_str


# 복호화
def s2j1c1_decrypt(value):
  key = os.getenv('PASSING_KEY', '3askdj1i2o3uq7sd8axzhqurhajsdhyg1238asdzjxcyew5ras')
  result = ""
  val_bytes = base64.b64decode(value)
  str_value = val_bytes.decode('ascii')
  for i in range((len(str_value)), 0, -1):
    k = i-1
    val2 = ord(str_value[k])
    key2 = ord(key[k%len(str_value)])
    
    val_res = val2^key2
    val_res_str = chr(val_res-len(str_value))
    
    result = val_res_str+result

  return result


# 코드값 가져오기
def code_down_value(up, down=None):
  q = Q()
  q.add(Q(code_up_code=up), q.AND)
  if down is not None:
    q.add(Q(code_down=down), q.AND)
  
  if down is not None:
    code_down_list = CodeDown.objects.get(q)
  else:
    code_down_list = CodeDown.objects.filter(q)
  
  return code_down_list
  
  
# 공공데이터 연결
def api_connect(type, option):
  if type == 'price':
    url = os.getenv('PRICE_URL')
  elif type == 'weather':
    url = os.getenv('PRICE_URL')
  
  params = {quote_plus('serviceKey'):os.getenv('DECODING_KEY')}
  for i, (k,v) in enumerate(option.items()):
    params[quote_plus(k)] = v
  
  queryParams = "?"+urlencode(params)
  
  res = requests.get(url + queryParams)
  xml = res.text
  soup = BeautifulSoup(xml, 'html.parser')
  
  # number of rows
  nor = soup.find('totalcount').text
  params[quote_plus('numOfRows')] = nor
  
  total_queryParams = "?"+urlencode(params)
  total_res = requests.get(url + total_queryParams)
  total_xml = total_res.text
  total_soup = BeautifulSoup(total_xml, 'html.parser')
  # print(total_soup)
  
  return total_soup