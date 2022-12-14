from django import forms
# from django.contrib.auth.models import User
from .models import Farm, Barn, User_Farm

# farm 등록 form
class FarmListForm(forms.ModelForm):
  farm_name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder":"농가명",
        "class" : "form-control",
        "readonly":"True"
      }
    ))
  company_num = forms.CharField(
    widget = forms.TextInput(
    attrs={
        "placeholder":"사업자번호",
        "class":"form-control",
        "readonly":"True"
      }
    ))
  farm_owner = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder": "대표자명",
        "class": "form-control",
        "readonly":"True"
      }
    ))
  farm_postcode = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder": "우편번호",
        "class": "form-control mb-1",
        "readonly":"True"
      }
    ))
  farm_addr1 = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder": "주소",
        "class": "form-control mb-1",
        "readonly":"True"
      }
    ))
  farm_addr2 = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder": "상세주소",
        "class": "form-control",
        "readonly":"True"
      }
    ))
  farm_tel_num = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder": "연락처",
        "class": "form-control",
        "readonly":"True"
      }
    ))
  
  class Meta:
    model = Farm
    fields = ('farm_name', 'company_num', 'farm_owner', 'farm_postcode', 'farm_addr1', 'farm_addr2', 'farm_tel_num')
  
class FarmInsertForm(forms.ModelForm):
    farm_code = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
            "placeholder" : "농가코드",
            "class" : "form-control"
        }
      ))
    farm_name = forms.CharField(
      required=True,
      widget=forms.TextInput(
          attrs={
              "placeholder":"농가명",
              "class" : "form-control"
          }
      ))
    company_num = forms.CharField(
      required=False,
      widget = forms.TextInput(
      attrs={
              "placeholder":"사업자번호",
              "class":"form-control",
              "oninput":"companyNumEvent(this);"
          }
      ))
    farm_owner = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
            "placeholder": "대표자명",
            "class": "form-control"
        }
      ))
    farm_postcode = forms.CharField(
      required=False,
      widget=forms.TextInput(
          attrs={
              "placeholder": "우편번호",
              "class": "form-control"
          }
      ))
    farm_addr1 = forms.CharField(
      required=False,
      widget=forms.TextInput(
          attrs={
              "placeholder": "주소",
              "class": "form-control"
          }
      ))
    farm_addr2 = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
            "placeholder": "상세주소",
            "class": "form-control"
        }
      ))
    farm_tel_num = forms.CharField(
      required=False,
      widget=forms.TextInput(
          attrs={
              "placeholder": "연락처",
              "class": "form-control",
              "oninput":"telNumEvent(this);"
          }
      ))
    class Meta:
      model = Farm
      fields = ('farm_code', 'farm_name', 'company_num', 'farm_owner', 'farm_postcode', 'farm_addr1', 'farm_addr2', 'farm_tel_num')

class FarmUpdateForm(forms.ModelForm):
    farm_code = forms.CharField(
      required=True,
      widget=forms.HiddenInput()
      )
    farm_name = forms.CharField(
      required=True,
      widget=forms.TextInput(
        attrs={
            "placeholder":"농가명",
            "class" : "form-control"
        }
      ))
    company_num = forms.CharField(
      required=False,
      widget = forms.TextInput(
      attrs={
          "placeholder":"사업자번호",
          "class":"form-control",
          "oninput":"companyNumEvent(this);"
        }
      ))
    farm_owner = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
          "placeholder": "대표자명",
          "class": "form-control"
        }
      ))
    farm_postcode = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
          "placeholder": "우편번호",
          "class": "form-control"
        }
      ))
    farm_addr1 = forms.CharField(
      required=False,
      widget=forms.TextInput(
          attrs={
              "placeholder": "주소",
              "class": "form-control"
          }
      ))
    farm_addr2 = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
            "placeholder": "상세주소",
            "class": "form-control"
        }
      ))
    farm_tel_num = forms.CharField(
      required=False,
      widget=forms.TextInput(
          attrs={
              "placeholder": "연락처",
              "class": "form-control",
              "oninput":"telNumEvent(this);"
          }
      ))
    class Meta:
      model = Farm
      fields = ('farm_code', 'farm_name', 'company_num', 'farm_owner', 'farm_postcode', 'farm_addr1', 'farm_addr2', 'farm_tel_num')

# barn 등록 form
class BarnInsertForm(forms.ModelForm):
    barn_name = forms.CharField(
      required=True,
      widget=forms.TextInput(
        attrs={
          "placeholder":"축사명",
          "class" : "form-control"
        }
      ))
    barn_info_scale = forms.CharField(
      required=False,
      widget = forms.TextInput(
        attrs={
          "placeholder":"축사규모",
          "class":"form-control"
        }
      ))
    barn_info_volumn = forms.CharField(
      required=False,
      widget=forms.TextInput(
        attrs={
          "placeholder": "축사용량",
          "class": "form-control"
        }
      ))
    barn_info_bigo = forms.CharField(
      required=False,
      widget=forms.Textarea(
        attrs={
          "placeholder": "축사설명",
          "class": "form-control"
        }
      ))

    class Meta:
      model = Barn
      fields = ('barn_name', 'barn_info_scale', 'barn_info_volumn', 'barn_info_bigo')

# barn 수정 form
class BarnUpdateForm(forms.ModelForm):
    barn_code = forms.IntegerField(
      required=True,
      widget=forms.HiddenInput(),
    )
    barn_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"축사명",
                "class" : "form-control"
            }
        )
    )
    barn_info_scale = forms.CharField(
        widget = forms.TextInput(
        attrs={
                "placeholder":"축사규모",
                "class":"form-control"
            }
        )
    )
    barn_info_volumn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "축사용량",
                "class": "form-control"
            }
        )
    )
    barn_info_bigo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "축사설명",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Barn
        fields = ('barn_code', 'barn_name', 'barn_info_scale', 'barn_info_volumn', 'barn_info_bigo')
