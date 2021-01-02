from django import forms
from django.forms import ModelForm

from user.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['status', 'created_time']
        labels = {
            'name': '姓名',
            'phone': '电话',
            'sex': '性别'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入姓名'
            })
        }
