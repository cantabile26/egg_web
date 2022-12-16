from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from users.models import User

class LoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder":"아이디",
        "class" : "form-control"
      }
    ))
  
  password = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "placeholder": "비밀번호",
            "class": "form-control"
        }
    ))

class SignUpForm(UserCreationForm):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        "placeholder":"아이디",
        "class" : "form-control"
      }
    ))
  nickname = forms.CharField(
    widget = forms.TextInput(
      attrs={
        "placeholder":"이름",
        "class":"form-control"
      }
    )
  )
  email = forms.EmailField(
    widget=forms.EmailInput(
        attrs={
            "placeholder": "이메일",
            "class": "form-control"
        }
    ))
  password1 = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "placeholder": "비밀번호",
            "class": "form-control"
        }
    ))
  password2 = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "placeholder": "비밀번호 확인",
            "class": "form-control"
        }
    ))
  
  class Meta:
    model = User
    fields = ('username', 'nickname', 'email', 'password1', 'password2')