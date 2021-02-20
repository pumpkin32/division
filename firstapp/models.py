from django.db import models
from django import forms

class db(models.Model):
    person = models.CharField(max_length = 50)
    message = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    
class dbForm(forms.Form):
    content = forms.CharField(label = '')
