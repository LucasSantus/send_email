from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Include URL APP's
    path('', include('home.urls')),
    path('', include('send.urls')),
]
