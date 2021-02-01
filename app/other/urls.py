from rest_framework.routers import SimpleRouter

from other import views

urlpatterns = []

router = SimpleRouter()
router.register(r'itunesapp', views.ItunesAppViewSet)
urlpatterns += router.urls
