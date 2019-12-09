from django.forms import ModelForm
from .models import Tracker

class Form(ModelForm):
    class Meta:
        model = Tracker
        fields = '__all__'
