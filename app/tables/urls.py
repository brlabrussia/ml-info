from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('preview/<int:id>/', views.preview, name='preview'),
]

router = DefaultRouter()
router.register(r'tables', views.TableViewSet, basename='table')
urlpatterns += router.urls
