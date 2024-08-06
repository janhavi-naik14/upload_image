from django.contrib import admin
from django.urls import path, include
from images.views import home
from images import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('images.urls')),
]

