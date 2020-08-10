from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('mfo/', include('lenders.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
