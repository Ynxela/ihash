from django.shortcuts import render
from datetime import datetime, timedelta
import hashlib
from .models import IHash
from .forms import IHashForm

def main(request, pk=None):

    form = IHashForm()

    title = 'iHash'
    if pk == None:
        links = IHash.objects.all()
    else:
        try:
            links = IHash.objects.all()[pk-1:pk]
        except:
            links = IHash.objects.all()
        print(links)

    content = {
        'title': title,
        'links': links,
        'form': form
    }

    return render(request, 'mainapp/index.html', context=content)