from django import forms
from .models import Contingent

modes = (('Cash','Cash'), ('Online','Online'),('PayTM','PayTM'),('GooglePay','GooglePay'))

class ContingentForm(forms.Form):
    contingent = forms.CharField()
    name = forms.CharField()
    phone = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    mode = forms.CharField(widget=forms.Select(choices=modes))
