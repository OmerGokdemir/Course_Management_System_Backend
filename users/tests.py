from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()

# Model Tests

class UserModelTest(TestCase):
    
    def test_create_user(self):
        user = User.objects.create_user(
            email="testuser@example.com",
            password="Testpass123",
            first_name="Test",
            last_name="User"
        )
        
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("Testpass123"))
        
        
    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="superuser@example.com",
            password="Superpass123"
        )
        
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)


#----------------------------------------------------------

# Serializers Tests

from rest_framework.test import APITestCase
from users.api.serializers import RegisterSerializer, ChangePasswordSerializer

class UserSerializerTest(APITestCase):
    
    def test_register_serializer(self):
        data = {
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "Newpass123"
        }
        
        serializer = RegisterSerializer(data=data)
        
        self.assertTrue(serializer.is_valid())
        
        user = serializer.save()
        
        self.assertEqual(user.email, "newuser@example.com")
        self.assertTrue(user.check_password("Newpass123"))
        
        
    def test_change_password_serializer(self):
        data = {
            "old_password": "Oldpass123",
            "new_password": "Newpass123"
        }
        
        serializer = ChangePasswordSerializer(data=data)
        
        self.assertTrue(serializer.is_valid())
        
        
#----------------------------------------------------------

# Views Tests

from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserViewTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="Testpass123",
            first_name="Test",
            last_name="User"
        )
        
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.token.access_token))
        
        
    def test_register_view(self):
        url = reverse("register-list")
        
        data = {
            "email": "newuser@example.com",
            "password": "Newpass123",
            "first_name": "New",
            "last_name": "User"
        }
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
        
    def test_change_password_view(self):
        url = reverse("change-password")
            
        data = {
            "old_password": "Testpass123",
            "new_password": "Newpass123"
        }
            
        response = self.client.put(url, data)
            
        self.assertEqual(response.status_code, status.HTTP_200_OK)