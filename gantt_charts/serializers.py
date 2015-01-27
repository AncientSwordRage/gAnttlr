
from rest_framework import serializers
from .models import Project, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'project', 'completed',)


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'title', 'tasks',)


