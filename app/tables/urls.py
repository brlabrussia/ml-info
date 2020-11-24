from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('preview/<int:id>/', views.preview, name='preview'),
    re_path(r'^scrapers/?$', views.ScrapersView.as_view()),
]

router = DefaultRouter()
router.register(r'tables', views.TableViewSet, basename='table')
urlpatterns += router.urls
