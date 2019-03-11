from django import forms
from pingtai.models import User
from .models import Article

class SelfInfoForm(forms.ModelForm):
  class Meta:
    model=User
    fields="__all__"
    exclude=['c','img']
    widgets = {
      'username': forms.TextInput(attrs={
        'class': 'input w50'
      }),
      'password': forms.TextInput(attrs={
        'class': 'input w50'
      }),
      'email': forms.EmailInput(attrs={
        'class': 'input w50'
      }),
      'tel': forms.TextInput(attrs={
        'class': 'input w50'
      })
    }

class ArticleForm(forms.ModelForm):
  class Meta:
    fields=['title','c','k','con','status']
    model=Article
