from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .routers import router
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import home
from drf_spectacular.views import  SpectacularAPIView,SpectacularSwaggerView



urlpatterns = [
    path('',home), # html template 
    path('admin/', admin.site.urls),
    # get token and refresh paths 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   # path('api/spots/',SpotsViewSet.as_view()),
 #   path('api/spots/<int:id>/',SpotsViewSet.as_view()),
    # path from router 
    path('api/',include(router.urls)),
    # donwload schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # swagger ui to check endpoints 
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'),
    name='swagger-ui')
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


