from django import forms
# from django.contrib.auth.models import User
from farm_management.models import Farm_Management

class FarmRegisterForm(forms.Form):
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
                "placeholder": "연락처",
                "class": "form-control"
            }
        )
    )
    farm_status = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "농가상태",
                "class": "form-control"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        farm_name = cleaned_data.get('farm_name')
        try:
            company_num = Farm_Management.objects.get(farm_name=farm_name)
        except Farm_Management.DoesNotExist:
            company_num = None
        print(company_num)
        if company_num:
            self.add_error('company_num', '이미 등록된 사업자번호입니다')


    class Meta:
        model = Farm_Management
        fields = ('farm_name', 'company_num', 'farm_owner', 'farm_postcode', 'farm_addr1', 'farm_addr2', 'farm_tel_num', 'farm_status')