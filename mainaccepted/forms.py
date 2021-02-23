from django.forms import ModelForm
from .models import submitEvent

class submitForm(ModelForm):
    class Meta:
        model = submitEvent
        fields = ['title', 'description', 'organisation']