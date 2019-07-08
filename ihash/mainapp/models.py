from django.db import models

class IHash(models.Model):
    tag_hash = models.CharField(max_length=64, verbose_name='хэш тега')
    link = models.CharField(max_length=256, verbose_name='ссылка')
    password_hash = models.CharField(max_length=64, verbose_name='хэш пароля', blank=True)
    date_created = models.DateTimeField(verbose_name='время создания')
    date_expiration = models.DateTimeField(verbose_name='время время удаления')
    is_active = models.BooleanField(verbose_name='активная ссылка или нет', default=True)
    counter_increases = models.PositiveIntegerField(default=0, verbose_name='сколько раз продлевали жизнь')
    client = models.PositiveIntegerField(default=1, verbose_name='откуда была добавлена ссылка. 1 - desctop, 2 - bot')
    ip_addr = models.CharField(max_length=64, blank=True, verbose_name='ip, с которого добавлена ссылка')

    def __str__(self):
        return self.link