from django.db import models
from django.contrib.auth.models import AbstractUser

class IHashUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='аватар')


class IHashUserLinks(models.Model):
    ihash_user = models.ForeignKey(IHashUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=256, verbose_name='ссылка')