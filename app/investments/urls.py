from rest_framework.routers import DefaultRouter

from investments import views

urlpatterns = []

router = DefaultRouter()
router.register(r'shares', views.ShareViewSet, basename='share')
urlpatterns += router.urls
