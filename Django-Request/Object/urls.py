
from django.http import HttpResponse
from django.urls import path, re_path
from Sadryev import views

urlpatterns = [
    path('',views.index),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)",views.user),
    re_path(r"^user",views.user),
    re_path('',views.error),
]
