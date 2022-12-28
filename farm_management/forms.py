from django import forms
# from django.contrib.auth.models import User
from farm_management.models import Farm_Management, Barn_Management

# farm 등록 form
class FarmInsertForm(forms.ModelForm):
    farm_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"농가명",
                "class" : "form-control"
            }
        )
    )
    company_num = forms.CharField(
        widget = forms.TextInput(
        attrs={
                "placeholder":"사업자번호",
                "class":"form-control"
            }
        )
    )
    farm_owner = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "대표자명",
                "class": "form-control"
            }
        )
    )
    farm_postcode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "우편번호",
                "class": "form-control"
            }
        )
    )
    farm_addr1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "주소",
                "class": "form-control"
            }
        )
    )
    farm_addr2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "상세주소",
                "class": "form-control"
            }
        )
    )
    farm_tel_num = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "-빼고 입력해주세요",
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = Farm_Management
        fields = ('farm_name', 'company_num', 'farm_owner', 'farm_postcode', 'farm_addr1', 'farm_addr2', 'farm_tel_num')


# barn 등록 form
class barnInsertForm(forms.ModelForm):
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
        widget=forms.TextInput(
            attrs={
                "placeholder": "축사설명",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Barn_Management
        fields = ('barn_name', 'barn_info_scale', 'barn_info_volumn', 'barn_info_bigo')