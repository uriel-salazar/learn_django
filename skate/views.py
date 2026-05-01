from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render
from .models import User,Spots
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,SpotSerializer
from rest_framework.views import APIView


def home(request):
    return render(request,'basic_home.html')

class UserView(APIView):
    
    
    def get(self, request):
    
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
    def post(self,request):
          serializer = UserSerializer(data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
          else:
              return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        try:
            user = User.objects.get(pk=id)
            data={
                "username": user.username,
                "email": user.email,
                "created_at":user.created_at
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        user = get_object_or_404(User,pk=id)
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        user = get_object_or_404(User,pk=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SpotsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        spots = Spots.objects.all()
        serializer = UserSerializer(spots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
   
    def post(self,request):
        
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class SpotsDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self,request,id):
        spots = get_object_or_404(Spots,pk=id)
        serializer = UserSerializer(spots,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        try:
            spots = Spots.objects.get(pk=id)
            data={
                "name_spot": spots.name_spot,
                "body": spots.body
            }
            return JsonResponse(data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
   
        

     

    