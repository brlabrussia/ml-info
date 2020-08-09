from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    re_path(r'^scrapers/cbr/$', views.CbrView.as_view()),
]
