from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404,render
from .models import User,Spots
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,SpotSerializer
from rest_framework.views import APIView


def home(request):
    return render(request,'basic_home.html')


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
 
class SpotsView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self,request,id=None):
        if id: # get user by id :
            try:
                spots = Spots.objects.get(pk=id)
                data={
                "name_spot": spots.name_spot,
                "body": spots.body
                }
                return JsonResponse(data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        # To get a list of users 
        spots = Spots.objects.all()
        serializer = SpotSerializer(spots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
   
    def post(self,request):
        
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        spots = get_object_or_404(Spots,pk=id)
        serializer = SpotSerializer(spots,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        """
        Deletes a spot, and if the spot isn't founded, it raises a 404 status code
        with a descriptive message. 
        """
        try:
            spot = Spots.objects.get(pk=id)
        except Spots.DoesNotExist:
                return Response({"error": " Not found"}, status=status.HTTP_404_NOT_FOUND)

        spot.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
   

class Ranking(APIView):
    pass

     

    