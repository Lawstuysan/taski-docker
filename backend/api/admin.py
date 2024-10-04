"""Configuration class for the API application."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """admin."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
