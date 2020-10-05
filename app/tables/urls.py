from django.urls import re_path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    re_path(r'^scrappers/?$', views.ScrapersView.as_view()),
]

router = DefaultRouter()
router.register(r'tables', views.TableViewSet, basename='table')
urlpatterns += router.urls
