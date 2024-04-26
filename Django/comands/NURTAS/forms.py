from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'city', 'age', 'school', 'course', 'birthday', 'specialty', 'ent_score', 'hobby']