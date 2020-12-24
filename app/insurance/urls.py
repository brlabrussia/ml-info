from rest_framework.routers import DefaultRouter

from insurance import views

urlpatterns = []

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)
urlpatterns += router.urls
