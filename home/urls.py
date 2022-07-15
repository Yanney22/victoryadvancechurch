from django.conf import settings
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, re_path, include
from django.contrib import admin

from home import views

urlpatterns = [
    # User Section Start
    path('', views.my_dashboard, name='home'),

    path('my-dashboard', views.my_dashboard, name='my_dashboard'),
    path('my-purchases', views.my_purchases, name='my_purchases'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
