from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
