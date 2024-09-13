from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api import views

router = DefaultRouter()

router.register(r"users", views.CustomUserViewSet, basename="users")
router.register(r"register", views.RegisterViewSet, basename="register")
router.register(r"login", views.LoginViewSet, basename="login")

urlpatterns = [
    path("", include(router.urls)),
    path("change-password/", views.ChangePasswordViewSet.as_view({"put": "update"}), name="change-password"),
]