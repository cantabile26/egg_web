from django.db import models

# Create your models here.

class Egginfo(models.Model):
    farm_code = models.BigIntegerField("농장코드")
    barn_code = models.BigIntegerField("축사코드")
    egg_code = models.BigAutoField(primary_key=True)
    egg_registration_date = models.CharField(max_length=100, null=False)
    egg_type = models.IntegerField()
    egg_number = models.BigIntegerField()