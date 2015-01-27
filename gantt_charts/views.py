from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Create your views here.

def project_list(request):
    projects = Project.objects.filter(tasks__isnull=False).order_by('updated_date').distinct()
    return render(request, 'project_list.html', {'projects':projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    messages.success(request, "Details for \""+project.title+"\"")
    return render(request, 'project_detail.html', {'project':project})

@login_required
def project_edit(request, project_id=None):

    # If we have a project ID, get that one
    if project_id:
        project = get_object_or_404(Project, pk=project_id)
        if project.owner != request.user and not request.user.is_superuser:
            response = HttpResponseForbidden()
            response.write("<p>You are not permitted to edit this project</p>")
            return response
    #Or we create a new one
    else:
        project = Project(owner=request.user)

    #Posting completed form
    if request.POST:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            return redirect('project_detail', project_id=project.pk, permanent=True)
    # Edit or create project
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project_edit.html', {'project':project, 'form':form})

@login_required
def task_edit(request, project_id=None, task_id=None):

    # If we have a task ID, get that one
    if task_id:
        task = get_object_or_404(Task.objects.select_related('project'), pk=task_id)
        if task.project.owner != request.user and not request.user.is_superuser:
            response = HttpResponseForbidden()
            response.write("<p>You are not permitted to edit this task</p>")
            return response
    #Or we create a new one
    else:
        task = Task(project=get_object_or_404(Project.objects.all(), pk=project_id))

    #Posting completed form
    if request.POST:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            # If the save was successful, redirect to another page
            return redirect('project_detail', project_id=task.project.pk, permanent=True)
    # Edit or create task
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_edit.html', {'task':task, 'form':form})

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ProjectSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticated,))
def project_json_list(request, format=None):
    """
    List all projects, or create a new project.
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def project_json_detail(request, pk, format=None):
    """
    Retrieve, update or delete a project.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
