from rest_framework import serializers
from .models import User
from django.forms import forms

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age','email']
    
    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Minimum 5 characters required.")
        return value