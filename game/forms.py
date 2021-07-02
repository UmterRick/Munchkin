from django.forms import ModelForm
from .models import Game


class Create_JoinForm(ModelForm):
    class Meta:
        model = Game
        fields = []
