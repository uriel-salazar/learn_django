from django.urls import path
from django.http import JsonResponse
from django.contrib import admin
from gym import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home)
]

