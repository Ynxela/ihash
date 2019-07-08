from django import forms
from .models import IHash

class IHashForm(forms.ModelForm):

    class Meta:
        model = IHash
        fields = ('tag_hash', 'link', 'password_hash')