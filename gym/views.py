from django.http import JsonResponse
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.views import APIView


def home(request):
    return JsonResponse({"ok": True})

class UserView(APIView):
    def get(self, request):
    
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
    def post(self,request,format=None):
          serializer = UserSerializer(data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
    def put(self,request):
         pass
    def delete(self,request):
         pass