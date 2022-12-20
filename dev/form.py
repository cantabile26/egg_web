from django import forms
from .models import CodeUp

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
    print(up_code)
    if up_code:
      self.add_error('code_up', "이미 있는 코드입니다.")
  
  
  class Meta:
    model = CodeUp
    fields = ('code_up', 'code_up_name', 'code_up_info')
    