from rest_framework import serializers
from .models import User,Spots
from django.forms import forms

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','password','created_at']
    
    
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # 🔐 hash
        user.save()
        return user
    
class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spots
        fields = ['id', 'name_spot', 'body', 'user', 'created_at']
        read_only_fields=['id','created_at']
        
        