from django.contrib import admin
from django.urls import path, include
from apps.todos.views import TaskViewSet
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register("task", TaskViewSet, basename="user_task")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("user/", include("apps.accounts.urls")),
]
