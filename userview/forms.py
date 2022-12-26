
from django import forms
from userview.models import *
from userview.admin import *
from django.db import models
from django import forms
from .models import *

class FaxForm(forms.ModelForm):
    class Meta:
        model = Fax
        fields ='__all__'
        widgets = {
            'name' : forms.TextInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4','required':'required'}),
            'email' : forms.TextInput({'class':'border w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4','required':'required'}),
            'message': forms.Textarea(attrs={'class':'border  w-96 text-black border-white block mb-4 rounded-lg text-gray/30 py-2 px-4', 'rows': 10, 'cols': 80}),
        }



# fields = ['name','file']