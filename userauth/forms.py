from django.forms import Form,ModelForm,Widget
from django import forms
from .models import User
from captcha.fields import CaptchaField
from django.core.validators import ValidationError
class RegisterForm(ModelForm):
    class Meta:
        model=User
        exclude=['img','c']
        widgets={
            'username':forms.TextInput(attrs={
                'class':"form_text_ipt"
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form_text_ipt"
            }),
            'email': forms.EmailInput(attrs={
                'class':"form_text_ipt"
            }),
            'tel': forms.TextInput(attrs={
                'class': "form_text_ipt"
            }),
        }
        labels={
            "username":"用户名",
            "password":"密码",
            "email":'邮箱',
            "tel":"手机号",
        }

class LoginForm(ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={
                'class': "form_text_ipt"
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form_text_ipt"
            }),
            'captcha': forms.PasswordInput(attrs={
                'class': "form_text_ipt"
            }),
        }
    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username',None)
        password=cleaned_data.get('password',None)
        if username and password:
            res=User.objects.filter(username=username,password=password).first()
            if not res:
                raise ValidationError("登录失败")
