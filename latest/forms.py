#Forrms for sportsite
from django import forms
from latest.models import Game

class NewSportForm(forms.ModelForm):
	class Meta:
		model=Game
