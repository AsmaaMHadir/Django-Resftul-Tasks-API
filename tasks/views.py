from django.shortcuts import render
from rest_framework import generics , permissions
from .serializers import TaskSerializer, UserSerializer, RegistrationSerializer
from .models import Task
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from rest_framework.reverse import reverse  

@api_view(["GET"])  # api entrypoint
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "tasks": reverse("tasks-list", request=request, format=format),
        }
    )

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    
    def perform_create(self, serializer):  # associates a task list with owner
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)
    
    '''
       def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        queryset = queryset.order_by('-id') 
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    '''
 
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all() # the set from which we query
    serializer_class = TaskSerializer # define the serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly) 
    
    
class UserList(generics.ListAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):  # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny,)
  serializer_class = RegistrationSerializer
    
    