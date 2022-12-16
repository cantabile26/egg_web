from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
  nickname = models.CharField("사용자 이름", max_length=50, null=False)
  user_type = models.CharField("사용자 타입", max_length=10, null=False)
  user_status = models.CharField("사용자 상태", max_length=10, null=False)
<<<<<<< HEAD
  user_email = models.EmailField("이메일", max_length=100, unique=True)
  passwrd     = models.CharField("비밀번호", max_length=256)
=======
  insert_id = models.CharField("insert id", max_length=100, null=True)
  insert_date = models.DateTimeField('insert date', null=True)
  update_id = models.CharField("update id", max_length=100, null=True)
  update_date = models.DateTimeField('update date', null=True)
  
>>>>>>> master
