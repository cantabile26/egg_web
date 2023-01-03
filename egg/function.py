import os
import base64

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
