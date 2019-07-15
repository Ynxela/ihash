from datetime import datetime, timedelta
from django.utils import timezone

from django.db import models


class IHashTag(models.Model):
    tag_hash = models.CharField(max_length=64, verbose_name='хеш названия тега')

    def __str__(self):
        return self.tag_hash


def get_expired_date():
    return timezone.now() + timedelta(days=30)


class IHashLink(models.Model):
    tag = models.ForeignKey(IHashTag, on_delete=models.CASCADE, related_name='ihashtag')
    link = models.CharField(max_length=256, verbose_name='ссылка')
    password_hash = models.CharField(max_length=64, verbose_name='хеш пароля', blank=True)
    date_created = models.DateTimeField(verbose_name='время создания', default=timezone.now)
    date_expiration = models.DateTimeField(verbose_name='время удаления', default=get_expired_date())
    is_active = models.BooleanField(verbose_name='активная ссылка или нет', default=True)
    ip_addr = models.GenericIPAddressField(protocol='both', verbose_name='ip, с которого добавлена ссылка')

    def __str__(self):
        return self.link

    