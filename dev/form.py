from django import forms
from dev.models import CodeUp, CodeDown
from django.db.models import Q
# 시작 상위코드 
# 상위코드 - insert form
class CodeInsertForm(forms.ModelForm):
  code_up = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(
      attrs={
        "placeholder" : "상위코드",
        "class" : "form-control"
      }
    ))
  
  code_up_name = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "상위코드명",
        "class" : "form-control"
      }
    ))
  
  code_up_info = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
        "placeholder":"상위코드 설명",
        "class" : "form-control"
      }
    )
  )
  
  def clean(self):
    cleaned_data = super().clean()
    code_up = cleaned_data.get('code_up')
    code_up_name = cleaned_data.get('code_up_name')
    try:
      up_code = CodeUp.objects.get(code_up=code_up)
    except CodeUp.DoesNotExist:
      up_code = None
    
    if up_code:
      self.add_error('code_up', "이미 있는 코드입니다.")
  
  
  class Meta:
    model = CodeUp
    fields = ('code_up', 'code_up_name', 'code_up_info')
    

# 상위코드 - update form
class CodeUdateForm(forms.ModelForm):
  code_up = forms.IntegerField(
    widget=forms.HiddenInput(),
    )
  code_up_name = forms.CharField(
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "상위코드명",
        "class" : "form-control"
      }
    ))
  code_up_info = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
        "placeholder":"상위코드 설명",
        "class" : "form-control"
      }
    )
  )
  class Meta:
    model = CodeUp
    fields = ('code_up', 'code_up_name', 'code_up_info', 'code_up_status')

# 시작 - 하위코드
class CodeDownInsertForm(forms.ModelForm):
  code_up_code_value = forms.IntegerField(
    widget=forms.HiddenInput(),
    )
  code_down = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(
      attrs={
        "placeholder" : "하위코드",
        "class" : "form-control"
      }
    ))
  code_value1 = forms.CharField(
    max_length=500,
    required=True,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값1",
        "class" : "form-control"
      }
    ))
  code_value2 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값2",
        "class" : "form-control"
      }
    ))
  code_value3 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값3",
        "class" : "form-control"
      }
    ))
  code_value4 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값4",
        "class" : "form-control"
      }
    ))
  code_value5 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값5",
        "class" : "form-control"
      }
    ))
  
  def clean(self):
    cleaned_data = super().clean()
    code_up_code = cleaned_data.get('code_up_code_value')
    code_down = cleaned_data.get('code_down')
    q = Q()
    q.add(Q(code_up_code=code_up_code), q.AND)
    q.add(Q(code_down=code_down), q.AND)
    
    try:
      code_down_data = CodeDown.objects.filter(q)
    except CodeDown.DoesNotExist:
      code_down_data = []
    
    if len(code_down_data) > 0:
      self.add_error('code_down', "이미 있는 코드입니다.")
  
  class Meta:
    model = CodeDown
    
    fields = ( 'code_down', 'code_value1', 'code_value2', 'code_value3', 'code_value4', 'code_value5')


class CodeDownUpdateForm(forms.ModelForm):
  code_up_code_value = forms.IntegerField(
    widget=forms.HiddenInput(),
    )
  code_down = forms.IntegerField(
    required=True,
    widget=forms.NumberInput(
      attrs={
        "placeholder" : "하위코드",
        "class" : "form-control",
        "readonly" : "True"
      }
    ))
  code_value1 = forms.CharField(
    max_length=500,
    required=True,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값1",
        "class" : "form-control"
      }
    ))
  code_value2 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값2",
        "class" : "form-control"
      }
    ))
  code_value3 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값3",
        "class" : "form-control"
      }
    ))
  code_value4 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값4",
        "class" : "form-control"
      }
    ))
  code_value5 = forms.CharField(
    max_length=500,
    required=False,
    widget=forms.TextInput(
      attrs={
        "placeholder" : "하위코드 값5",
        "class" : "form-control"
      }
    ))
  
  class Meta:
    model = CodeDown
    
    fields = ( 'code_down', 'code_value1', 'code_value2', 'code_value3', 'code_value4', 'code_value5')
# 종료 - 하위코드