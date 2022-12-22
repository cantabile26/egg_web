from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from egg_info.models import Egginfo

class Egg_Info_Form(forms.Form):
  farm_code = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "class" : "form-control",
        'placeholder':'Farm_code',
      }
    ))
  barn_code = forms.CharField(
    widget=forms.TextInput(
        attrs={
        "class" : "form-control",
        'placeholder':'Barn_code',
      }
    ))
  egg_registration_date = forms.DateTimeField(
    widget=forms.DateTimeInput(
        attrs={
        "class" : "form-control",
        'placeholder':'Egg_registraion_date',
      }
    ))
  egg_type = forms.CharField(
    widget=forms.TextInput(
        attrs={
        "class" : "form-control",
        'placeholder':'Egg_type',
      }
    ))
  egg_number = forms.IntegerField(
    widget=forms.NumberInput(
        attrs={
        "class" : "form-control",
        'placeholder':'Egg_number',
      }
    ))

  class Meta:
    model = Egginfo
    fields = ( 'farm_code', 'barn_code', "egg_registration_date", 'egg_type', 'egg_number')