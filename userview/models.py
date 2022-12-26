from django.db import models
from django import forms
from userview.models import *
from django.contrib import admin


class FaxForm(forms.Form):
    name = forms.CharField( max_length=100)
    email = forms.EmailField( max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'my-textarea', 'rows': 10, 'cols': 80}))

    def nama(self):
        return self.name 
      

    
# Create your models here.

# class UploadedFile(models.Model):
#     name = models.CharField(blank=True, null=True, max_length=100)
#     file = models.FileField(upload_to='static/legenda/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
    
#     def nama(self):
#         return self.name 
