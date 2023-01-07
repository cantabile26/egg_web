from django import forms
from .models import Accounting

class BoardForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = ['farm_code', 'barn_code', '회계코드','계좌번호','출납일','발의일']
