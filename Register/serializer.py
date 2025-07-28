from rest_framework import serializers
from .models import *

# Simple Serializer
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=10)
    email = serializers.EmailField(unique=True)
    created_at = serializers.DateField(auto_now_add=True)
    updated_at = serializers.DateField(auto_now= True)

def create(self, validated_data):
    return User.objects.create(**validated_data)

# ModelSerializer
class userProfileSerializer(serializers.ModelSerializer):
    class meta:
        model = userProfile
        fields = '__all__'

# nested Serializer
class verificationCodeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class meta:
        model = verificationCode
        fields = ['id', 'code', 'is_verified', 'user']
