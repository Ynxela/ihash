from django.contrib import admin

from .models import IHashLink, IHashTag

# Register your models here.

admin.site.register(IHashLink)
admin.site.register(IHashTag)