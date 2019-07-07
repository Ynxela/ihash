from django.db import models

class IHash(models.Model):
    tag_hash = models.CharField(max_length=64, verbose_name='хэш тега')
    link = models.CharField(max_length=256, verbose_name='ссылка')
    password_hash = models.CharField(max_length=64, verbose_name='хэш пароля', blank=True)
    date_created = models.DateTimeField(verbose_name='время создания')
    date_expiration = models.DateTimeField(verbose_name='время время удаления')
    is_active = models.BooleanField(verbose_name='активная ссылка или нет')
    counter_increases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.link