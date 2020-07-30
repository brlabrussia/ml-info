from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lenders/', include('lenders.urls')),
    path('admin/', admin.site.urls),
]
