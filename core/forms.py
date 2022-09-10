from attr import fields
from django import forms
from django import forms
from core.models import Contact_me 
class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact_me
        fields='__all__'