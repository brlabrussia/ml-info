from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    re_path(r'^scrapers/cbr/$', views.CbrView.as_view()),
]

router = DefaultRouter()
router.register(r'lenders', views.LenderViewSet, basename='lender')
router.register(r'loans', views.LoanViewSet, basename='loan')
urlpatterns += router.urls
