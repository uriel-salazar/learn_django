from rest_framework import serializers
from .models import User,Spots,Rating
from decimal import Decimal
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile



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
        fields = ['id', 'name_spot','image_url','body', 'created_at']
        read_only_fields=['id','created_at','user']
        
    def create(self,validated_data):
        instance = super().create(validated_data)
        original_name = instance.image_url.name
        
        if instance.image_url:
            #function that resizes the image 
            resized_image=image_resize_800(instance.image_url)
    
            instance.image_url.delete(save=False) # Deletes original image 
            instance.image_url.save(
            original_name,  # using original url name 
            ContentFile(resized_image.getvalue()),# Extract values from BytesIO
            save=True
        )

        return instance
            
            
class RatingSerializer(serializers.ModelSerializer):
        # We use a serializer method field to use the method get_<field_name>
        score = serializers.SerializerMethodField()
        class Meta:
            model = Rating
            fields = "__all__"
            read_only_fields=['id','created_at','user_id','spot_id']
        
        # Return it as decimal 
        def get_score(self,column):
            return Decimal(column.score)
            
        
    