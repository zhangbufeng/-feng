from django import forms
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        fields="__all__"
        model=UserInfo

        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'admin_input_style'
            }),
            'position': forms.TextInput(attrs={
                'class': 'admin_input_style'
            }),
            'honny': forms.TextInput(attrs={
                'class': 'admin_input_style'
            }),
            'reason': forms.Textarea(attrs={
                'class': 'admin_input_style'
            }),
            'realname': forms.TextInput(attrs={
                'class': 'admin_input_style'
            }),
        }