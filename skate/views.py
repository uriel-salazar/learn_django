from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.views import APIView


def home(request):
    return JsonResponse({"ok": True},)

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
    def get(self,request,id):
        try:
            user = User.objects.get(pk=id)
            data={
                "name": user.name,
                "age": user.age,
                "email": user.email
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
        

     

    