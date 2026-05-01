from django.urls import path,include
from django.http import JsonResponse
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from skate import views
from .views import UserView,UserDetail,SpotsView,SpotsDetail,home

urlpatterns = [
    path('',home), # html template 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('users/',UserView.as_view()),
    path('users/<int:id>/',UserDetail.as_view()),
    path('spots/',SpotsView.as_view()),
    path('spots/<int:id>/',SpotsDetail.as_view())
]


