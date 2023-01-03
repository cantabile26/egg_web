
from django.db import models
from users.models import User
from django.utils import timezone

class Farm(models.Model):
  farm_code = models.CharField("농가코드", max_length=500, primary_key=True)
  farm_name = models.CharField("농가명", max_length=100, null=False)
  company_num = models.CharField("사업자번호", max_length=100, null=True)
  farm_owner = models.CharField("대표자명", max_length=50, null=True)
  farm_postcode = models.CharField("우편번호", max_length=20, null=True)
  farm_addr1 = models.CharField("주소", max_length=500, null=True)
  farm_addr2 = models.CharField("상세주소", max_length=500, null=True)
  farm_tel_num = models.CharField("연락처", max_length=100, null=True)
  farm_status = models.CharField("농가상태", max_length=10, null=False)
  insert_id = models.CharField("insert id", max_length=100, null=True)
  insert_date = models.DateTimeField('insert date', null=True)
  update_id = models.CharField("update id", max_length=100, null=True)
  update_date = models.DateTimeField('update date', null=True)
  
  class Meta:
    ordering = ['insert_date']
  
  def save(self, *args, **kwargs):
    if not self.farm_code:
      self.insert_date = timezone.localtime()
    else:
      self.update_date = timezone.localtime()
    
    super(Farm, self).save(*args, **kwargs)

# 축사 관리 모델
class Barn(models.Model):
    farm_farm_code = models.ForeignKey("Farm", related_name="농가코드", on_delete=models.CASCADE, db_column="farm_farm_code")
    barn_code = models.BigAutoField("축사코드", primary_key=True)
    barn_name = models.CharField("축사이름", max_length=100, null=False)
    barn_info_scale = models.CharField("축사규모", max_length=50, null=True)
    barn_info_volumn = models.CharField("축사용량", max_length=50, null=True)
    barn_info_bigo = models.CharField("축사설명", max_length=50, null=True)
    insert_id = models.CharField("insert id", max_length=100, null=True)
    insert_date = models.DateTimeField('insert date', null=True)
    update_id = models.CharField("update id", max_length=100, null=True)
    update_date = models.DateTimeField('update date', null=True)

    def save(self, *args, **kwargs):
      if not self.barn_code:
        self.insert_date = timezone.localtime()
      else:
        self.update_date = timezone.localtime()
      super(Barn, self).save(*args, **kwargs)
        
class User_Farm(models.Model):
  user_farm_idx = models.BigAutoField(primary_key=True)
  
  user_id = models.ForeignKey(User, related_name="유저고유값", on_delete=models.CASCADE, db_column="user_id")
  farm_farm_code = models.ForeignKey("Farm", related_name="uf_농가코드", on_delete=models.CASCADE, db_column="farm_farm_code")

  