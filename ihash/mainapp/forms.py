from django import forms
from .models import IHash

class IHashForm(forms.ModelForm):

    class Meta:
        model = IHash
        fields = ('tag_hash', 'link', 'password_hash')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field'