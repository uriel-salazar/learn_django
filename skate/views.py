
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render,get_object_or_404
from .models import User,Spots,Rating
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,SpotSerializer,RatingSerializer
from rest_framework.pagination import LimitOffsetPagination


def home(request):
    return render(request,'basic_home.html')


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SpotsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset= Spots.objects.all()
    pagination_class = LimitOffsetPagination
    parser_classes = (MultiPartParser, FormParser)
    serializer_class= SpotSerializer
    
  #  injects to the actual user before saving it.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class RatingViewSet(ModelViewSet):
    
    serializer_class = RatingSerializer
    mini_serializer_class= RatingSerializer
    queryset = Rating.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        spot = get_object_or_404(
                Spots,
                pk=self.kwargs['spots_id']
            )

        serializer.save(
                user=self.request.user,
                spot=spot
            )

    