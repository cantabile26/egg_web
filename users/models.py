from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  nickname = models.CharField("사용자 이름", max_length=50, null=False)
  user_type = models.CharField("사용자 타입", max_length=10, null=False)
  user_status = models.CharField("사용자 상태", max_length=10, null=False)