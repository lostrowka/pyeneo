from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('make_a_request/', views.request_page, name='request_page'),
    # path('output/<str:task_id>/', views.output_page, name='output_page'),
    # path('loading/<str:task_id>/', views.loading_page, name='loading_page'),
    # path('check_output/<str:task_id>/', views.check_output, name='check_output'),
    path('', views.redirect_to_request, name='redirect_to_request_page'),
]

urlpatterns += staticfiles_urlpatterns()
