from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('tables/', include('tables.urls')),
   path('insurance/', include('insurance.urls')),
   path('other/', include('other.urls')),

   path('api/v1/', include('api.v1.urls')),

   re_path(r'^api-auth/', include('rest_framework.urls')),
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
