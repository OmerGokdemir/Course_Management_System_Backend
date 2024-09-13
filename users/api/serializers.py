from rest_framework import serializers
from users.models import CustomUser
import re
from django.contrib.auth import authenticate



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "is_active", "is_staff"]
        
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "password"]
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", "")
        )
        
        return user
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
    def validate_new_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError("New Password must be at least 8 characters long.")
        
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("New Password must be contain at least one uppercase letter.")
        
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("New Password must be contain at least one lowercase letter.")
        
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("New Password must be contain at least one digit.")
        
        return value
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        
        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)
            
            if not user:
                raise serializers.ValidationError("Invalid email or password.")
            
        else:
            raise serializers.ValidationError("Both email and password are required.")
        
        data["user"] = user
        return data