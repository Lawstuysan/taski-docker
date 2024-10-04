"""Serializers for the API application."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Configuration class for the API application."""

    class Meta:
        """Configuration class for the API application."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
