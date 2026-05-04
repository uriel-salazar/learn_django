from rest_framework.routers import DefaultRouter
from .views import UserViewSet,SpotsView
router = DefaultRouter()

router.register(r'users', UserViewSet)


