from django import forms
from .models import Eventos


class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['evento', 'local', 'data']