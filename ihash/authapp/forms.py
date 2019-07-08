from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import IHashUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = IHashUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'ihash-form'