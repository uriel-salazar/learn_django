
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render
from .models import User,Spots,Rating
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,SpotSerializer,RatingSerializer
from rest_framework.views import APIView


def home(request):
    return render(request,'basic_home.html')


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class SpotsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset= Spots.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class= SpotSerializer
    
  #  injects to the actual user before saving it.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class RatingViewSet(ModelViewSet):
    
    serializer_class = RatingSerializer
    mini_serializer_class= RatingSerializer
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    
    

     

    