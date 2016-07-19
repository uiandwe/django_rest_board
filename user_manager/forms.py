__author__ = 'uiandwe'

from django import forms


class LoginForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12, widget=forms.PasswordInput)


class JoinForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12, widget=forms.PasswordInput)
    password_check = forms.CharField(label="PASSWORD(again)", min_length=6, max_length=12, widget=forms.PasswordInput,
                                     error_messages={'min_length': '에러! %(limit_value)d 이상 입력해주셈'})