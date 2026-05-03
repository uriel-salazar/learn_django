from django.urls import path,include
from django.contrib import admin
from .routers import router
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import SpotsView,SpotsDetail,home


urlpatterns = [
    path('',home), # html template 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('spots/',SpotsView.as_view()),
    path('spots/<int:id>/',SpotsDetail.as_view())
]


