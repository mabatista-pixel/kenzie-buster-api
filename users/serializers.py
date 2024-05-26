from rest_framework import serializers, status, permissions
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField()
    birthdate = serializers.DateField(required=False)
    is_employee = serializers.BooleanField(required=False, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already registered.")
        return value
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already taken.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            birthdate=validated_data.get('birthdate'),
            is_employee=validated_data.get('is_employee', False)
        )
        user.set_password(validated_data['password'])

        if user.is_employee:
            user.is_superuser = True
        else:
            user.is_superuser = False

        user.save()

        return user
    
    def update(self, instance: User, validated_data: dict):

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:    
                setattr(instance, key, value)

        instance.save()
        return instance
    

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser

        return token
    
