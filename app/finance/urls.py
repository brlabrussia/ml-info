from rest_framework.routers import SimpleRouter

from finance import views

urlpatterns = []

router = SimpleRouter()
router.register(r'person', views.PersonViewSet)
urlpatterns += router.urls
