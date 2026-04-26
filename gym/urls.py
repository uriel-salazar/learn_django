from django.urls import path
from django.http import JsonResponse
from django.contrib import admin
from gym import views
from .views import UserView,UserDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',UserView.as_view()),
    path('users/<int:id>/',UserDetail.as_view())
]


