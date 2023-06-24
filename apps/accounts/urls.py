from .views import UserCreateAPI
from django.urls import path, include

urlpatterns = [
    path("register/", UserCreateAPI.as_view(), name="register"),
]
