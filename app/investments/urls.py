from rest_framework.routers import DefaultRouter

from investments import views

urlpatterns = []

router = DefaultRouter()
router.register(r'shares', views.ShareViewSet, basename='share')
router.register(r'bonds', views.BondViewSet, basename='bond')
router.register(r'iias', views.IIAViewSet, basename='iia')
urlpatterns += router.urls
