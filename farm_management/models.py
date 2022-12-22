from django.db import models

# Create your models here.

class Farm_Management(models.Model):
    farm_name = models.CharField("농가명", max_length=100, null=False)
    company_num = models.CharField("사업자번호", max_length=100, null=True)
    farm_owner = models.CharField("대표자명", max_length=50, null=True)
    farm_postcode = models.CharField("우편번호", max_length=20, null=True)
    farm_addr1 = models.CharField("주소", max_length=500, null=True)
    farm_addr2 = models.CharField("상세주소", max_length=500, null=True)
    farm_tel_num = models.CharField("연락처", max_length=100, null=True)
    farm_status = models.CharField("농가상태", max_length=10, null=False)