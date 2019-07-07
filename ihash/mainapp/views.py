from django.shortcuts import render
from datetime import datetime, timedelta
import hashlib

def main(request):
    title = 'iHash'
    links = [
        {
            'link': 'http://vk.com',
            'date': '12:24:13 11.06.2019',
            'can_modify': True,
            'date_expired': '12:24:13 11.07.2019',
            'password_hash': {
                'is_hash': True,
                'hash': 'hash'
            }
        },
    ]
    content = {
        'title': title,
        'links': links,
    }
    return render(request, 'mainapp/index.html', context=content)