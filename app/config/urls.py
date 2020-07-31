from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mfo/', include('lenders.urls')),
    path('admin/', admin.site.urls),
]
