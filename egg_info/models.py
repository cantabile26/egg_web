from django.db import models

# Create your models here.

class Egginfo(models.Model):
    farm_code = models.CharField("농장코드", max_length=50, null=False)
    barn_code = models.CharField("축사코드", max_length=50, null=False)
    egg_registration_date = models.DateTimeField("egg_registration_date", null=True)
    egg_type = models.CharField("egg_type", max_length=50, null=False)
    egg_number = models.BigIntegerField("egg_number", null=False)