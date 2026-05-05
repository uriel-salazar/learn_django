from rest_framework import serializers
from .models import User,Spots
from django.forms import forms
from PIL import Image
from io import BytesIO



def image_resize_800(file):


    image = Image.open(file)
            
    image.thumbnail((800, 800))
    
    output = BytesIO()
    image.save(output, format=image.format or "JPEG",quality=85)
    output.seek(0)
    return output

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
            raise serializers.ValidationError(f"'{username}' must have at least 5 words.")
        return username
    
class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Spots
<<<<<<< HEAD
        fields = ['id', 'name_spot', 'body', 'created_at']
=======
        fields = ['id', 'name_spot','image_url','body', 'created_at']
>>>>>>> work
        read_only_fields=['id','created_at','user']
        
    def create(self,validated_data):
        instance = super().create(validated_data)
        if instance.image_url:
            resized_image=image_resize_800(instance.image_url)
        #Saves resized image 
            instance.image_url.save(
            instance.image_url.name,
            resized_image,
            save=True
            )
        return instance
            
            

        