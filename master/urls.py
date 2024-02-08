from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
]
