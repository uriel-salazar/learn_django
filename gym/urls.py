from django.urls import path
from django.http import JsonResponse
from django.contrib import admin
from gym import views
from .views import UserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',UserView.as_view())
]

