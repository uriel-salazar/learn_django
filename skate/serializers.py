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
        user.set_password(validated_data['password'])  
        user.save()
        return user
    # An username has to have at least 5 words 
    def validate_username(self, username):
        if len(username.split()) < 5:
            raise serializers.ValidationError("At least 5 words required.")
        return username
    
class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spots
        fields = ['id', 'name_spot', 'body', 'created_at']
        read_only_fields=['id','created_at','user']
        
        