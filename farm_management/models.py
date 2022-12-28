from django.db import models

# Create your models here.

class Farm_Management(models.Model):
    farm_code = models.BigAutoField("농가코드", primary_key=True, auto_created=True)
    farm_name = models.CharField("농가명", max_length=100, null=False)
    company_num = models.CharField("사업자번호", max_length=100, null=True)
    farm_owner = models.CharField("대표자명", max_length=50, null=True)
    farm_postcode = models.CharField("우편번호", max_length=20, null=True)
    farm_addr1 = models.CharField("주소", max_length=500, null=True)
    farm_addr2 = models.CharField("상세주소", max_length=500, null=True)
    farm_tel_num = models.CharField("연락처", max_length=100, null=True)
    farm_status = models.CharField("농가상태", max_length=10, null=False)

    def save(self, *args, **kwargs):
        super(Farm_Management, self).save(*args, **kwargs)


class Barn_Management(models.Model):
    # farm_code_id = models.ForeignKey("Farm_Management", related_name="농가코드", on_delete=models.CASCADE, db_column="farm_barn")
    barn_code = models.BigAutoField("축사코드", primary_key=True, auto_created = True)
    barn_name = models.CharField("축사이름", max_length=50, null=False)
    barn_info_scale = models.CharField("축사규모", max_length=50, null=False)
    barn_info_volumn = models.CharField("축사용량", max_length=50, null=False)
    barn_info_bigo = models.CharField("축사설명", max_length=50, null=False)

    def save(self, *args, **kwargs):
        super(Barn_Management, self).save(*args, **kwargs)