__author__ = 'uiandwe'

from django import forms


class LoginForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12, widget=forms.PasswordInput)


class JoinForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12, widget=forms.PasswordInput)
    password_check = forms.CharField(label="PASSWORD(again)", max_length=12, widget=forms.PasswordInput)