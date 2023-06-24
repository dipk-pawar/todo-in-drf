from .models import Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()

    class Meta:
        model = Task
        exclude = ["created_at", "updated_at"]
