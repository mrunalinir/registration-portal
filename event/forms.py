from django import forms
from .models import Event

modes = (('Cash','Cash'), ('Online','Online'),('PayTM','PayTM'),('GooglePay','GooglePay'))

class EventForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    college = forms.CharField()
    mode = forms.CharField(widget=forms.Select(choices=modes))
