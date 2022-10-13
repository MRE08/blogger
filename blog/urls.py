from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index , name='index')
]

#Important to link the static files uploads to django
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
