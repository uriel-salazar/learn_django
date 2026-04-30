from django.urls import path
from django.http import JsonResponse
from django.contrib import admin
from skate import views
from .views import UserView,UserDetail,SpotsView,SpotsDetail,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('users/',UserView.as_view()),
    path('users/<int:id>/',UserDetail.as_view()),
    path('spots/',SpotsView.as_view()),
    path('spots/<int:id>/',SpotsDetail.as_view())
]


