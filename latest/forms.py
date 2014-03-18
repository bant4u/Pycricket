#Forrms for sportsite
from django import forms
from latest.models import Game
from django.contrib.auth.models import User

class NewSportForm(forms.ModelForm):
	class Meta:
		model=Game

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')