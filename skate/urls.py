from django.urls import path
from django.contrib import admin
from .routers import router
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import SpotsView,SpotsDetail,home


urlpatterns = [
    path('',home), # html template 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/',router.urls),
    path('admin/', admin.site.urls),
    path('spots/',SpotsView.as_view()),
    path('spots/<int:id>/',SpotsDetail.as_view())
]


