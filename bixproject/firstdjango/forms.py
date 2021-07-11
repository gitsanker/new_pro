from django import forms
from .models import myform
class formclass(forms.ModelForm):
    name = forms.CharField(required=True)
    mobilenumber = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model=myform
        fields=('name', 'mobilenumber', 'email')