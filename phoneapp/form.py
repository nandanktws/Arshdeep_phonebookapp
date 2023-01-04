from django import forms
from django.forms import ModelForm

from .models import *
#from .form import *

class ContactForm(forms.ModelForm):
    
    
    class Meta:
        model = Phonebook
        fields = '__all__'