
from django.db import models


class Accounting(models.Model):
  farm_code = models.IntegerField("농장 번호", max_length=50, null=False)
  barn_code = models.CharField("사업자 등록번호", max_length=10, null=False, unique=True)
  회계코드 = models.CharField("회계코드", max_length=10, null=False, unique=True)
  계좌번호 = models.IntegerField("계죄번호", max_length=100, unique=True)
  출납일     = models.DateTimeField("출납일", auto_now=False, auto_now_add=False)
  발의일     = models.DateTimeField("발의일", auto_now=False, auto_now_add=False)
  결제일     = models.DateTimeField("결제일", auto_now=False, auto_now_add=False)
  등기일     = models.DateTimeField("등기일", auto_now=False, auto_now_add=False)
  결의구분     = models.BooleanField("결의구분",max_length=1)
  계정과목     = models.CharField("계정과목", max_length=256)
  적요     = models.CharField("적요", max_length=256)
  수입     = models.IntegerField("수입", max_length=256)
  지출     = models.IntegerField("지출", max_length=256)
  자금원천     = models.CharField("자금원천", max_length=256)
  정렬     = models.CharField("정렬", max_length=256)
  비고     = models.CharField("비고", max_length=256)
