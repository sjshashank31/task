from django.shortcuts import render, HttpResponse
from rest_framework import status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from .models import Task, Role
from rest_framework.views import exception_handler
from django.contrib.auth.decorators import login_required

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def create_task(request):
    user = request.data['user']
    role = get_object_or_404(Role, user=user)

    if str(role) == "C":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('Only Clients can create Tasks')


@api_view(['POST'])
def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if str(request.user.role.role) == "M":
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('Only Manager can edit Task')


@api_view(['DELETE'])
def delete_task(request, pk):
    if str(request.user.role.role) == "M":
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response("Task Successfully deleted")
    else:
        return Response('Only Manager can delete Task')



@api_view(['POST'])
def assign_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if str(request.user.role.role) == "M":
        serializer = TaskAssignSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    else:
        return Response('Only Manager can Assign Task')


@api_view(['POST'])
def change_status(request, pk):
    task = get_object_or_404(Task, id=pk)
    if str(request.user.role.role) == "E":
        serializer = TaskStatusSerializer(instance=task, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response('Only Employee can change status of task')






