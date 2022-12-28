from django.db import models
from django.utils import timezone

class CodeUp(models.Model):
  code_up = models.BigIntegerField('상위코드', primary_key=True)
  code_up_name = models.CharField('상위코드 명', max_length=100, null=False)
  code_up_info = models.TextField('상위코드 설명', null=True)
  code_up_status = models.CharField('상위코드 상태', max_length=10, default='show')
  insert_id = models.CharField("insert id", max_length=100, null=True)
  insert_date = models.DateTimeField('insert date', null=True)
  update_id = models.CharField("update id", max_length=100, null=True)
  update_date = models.DateTimeField('update date', null=True)
  
  class Meta:
    verbose_name = "Code Up"
    verbose_name_plural = "Code Up"
    ordering = ['code_up']
  
  def save(self, *args, **kwargs):
    if not self.code_up:
      self.insert_date = timezone.localtime()
    else:
      self.update_date = timezone.localtime()
    
    super(CodeUp, self).save(*args, **kwargs)
    

class CodeDown(models.Model):
  code_up_code = models.ForeignKey("CodeUp", related_name="상위코드", on_delete=models.CASCADE, db_column="code_up_code")
  code_down = models.BigIntegerField("하위코드", null=False)
  code_value1 = models.CharField("값1", max_length=500)
  code_value2 = models.CharField("값1", max_length=500)
  code_value3 = models.CharField("값1", max_length=500)
  code_value4 = models.CharField("값1", max_length=500)
  code_value5 = models.CharField("값1", max_length=500)  
  code_down_status = models.CharField('하위코드 상태', max_length=10, default='show')
  insert_id = models.CharField("insert id", max_length=100, null=True)
  insert_date = models.DateTimeField('insert date', null=True)
  update_id = models.CharField("update id", max_length=100, null=True)
  update_date = models.DateTimeField('update date', null=True)
  
  class Meta:
    verbose_name = "Code down"
    verbose_name_plural = "Code down"
    
    constraints = [
      models.UniqueConstraint(
        fields=["code_up_code", "code_down"],
        name="unique code_up_down"
      )
    ]
  
  def save(self, *args, **kwargs):
    if not self.code_down:
      self.insert_date = timezone.localtime()
    else:
      self.update_date = timezone.localtime()
    
    super(CodeDown, self).save(*args, **kwargs)
  