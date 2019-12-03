from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.request_page, name='request_page'),
]

urlpatterns += staticfiles_urlpatterns()
