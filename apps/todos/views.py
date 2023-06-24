from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializers
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializers

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
