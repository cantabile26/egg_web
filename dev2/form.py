from django import forms
from users.models import User


class BoardForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'user_type', 'user_status']

