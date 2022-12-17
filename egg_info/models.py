from django.db import models


# Create your models here.

class Egginfo(models.Model):
    farm_code = models.CharField("농장 이름", max_length=50, null=True)
    barn_code = models.CharField("축사 이름", max_length=50, null=False)
    egg_registration_date = models.DateTimeField("egg_registration_date")
    egg_type = models.CharField("egg_type", max_length=50, null=False)
    egg_number = models.BigIntegerField("egg_number", null=False)
