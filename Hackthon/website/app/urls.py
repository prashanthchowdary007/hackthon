from django.urls import path
from .views import Home, uploadedImgs, Mail_Service
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name='Home'),
    path('website/', uploadedImgs, name='db_imgs'),
    path('mail/',Mail_Service, name='mail')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
