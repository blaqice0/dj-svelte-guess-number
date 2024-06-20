from django.contrib import admin
from django.urls import path

from spa.views import app_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_view, name='app'),
]
