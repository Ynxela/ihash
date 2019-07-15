import hashlib

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import IHashCreateForm, IHashReadForm
from .models import IHashLink, IHashTag


def main(request, hash=None):
    title = 'iHash'

    create_form = IHashCreateForm()
    search_form = IHashReadForm()

    links = []

    if hash is not None:
        try:
            tag = IHashTag.objects.get(tag_hash=hash)
            links = IHashLink.objects.filter(tag=tag).order_by('-date_created')
        except:
            pass

    content = {
        'title': title,
        'links': links,
        'create_form': create_form,
        'search_form': search_form
    }

    return render(request, 'mainapp/index.html', context=content)


def create(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        tag = request.POST.get('tag')
        ip_addr = request.META.get('REMOTE_ADDR')
        password = request.POST.get('password')
        new_tag_hash = hashlib.sha256(tag.encode()).hexdigest()

        old_tag = IHashTag.objects.filter(tag_hash=new_tag_hash)

        if old_tag:
            new_tag = old_tag[0]
        else:
            new_tag = IHashTag(tag_hash=new_tag_hash)
            new_tag.save()

        new_link = IHashLink(tag=new_tag, link=link, ip_addr=ip_addr)

        if password:
            new_link.password_hash = hashlib.sha256(password.encode()).hexdigest()

        new_link.save()

        return HttpResponseRedirect(reverse('main', kwargs={'hash': new_tag_hash}))


def read(request):
    tag = request.POST.get('tag')
    new_tag_hash = hashlib.sha256(tag.encode()).hexdigest()
    return HttpResponseRedirect(reverse('main', kwargs={
        'hash': new_tag_hash}))


def update(request):
    pass


def delete(requesst):
    pass
