from rest_framework.routers import SimpleRouter

from banks import views

urlpatterns = []

router = SimpleRouter()
router.register(r'rating', views.RatingViewSet)
urlpatterns += router.urls
