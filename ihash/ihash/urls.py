
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('<str:hash>', mainapp.main, name='main'),
    path('create/', mainapp.create, name='create'),
    path('delete/<int:pk>', mainapp.delete, name='delete'),
    path('read/', mainapp.read, name='read'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
