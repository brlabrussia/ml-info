from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tables', views.TableViewSet, basename='table')
urlpatterns = router.urls
