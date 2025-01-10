from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        completed_todos = Todo.objects.filter(completed=True)
        serializer = self.get_serializer(completed_todos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def incomplete(self, request):
        incomplete_todos = Todo.objects.filter(completed=False)
        serializer = self.get_serializer(incomplete_todos, many=True)
        return Response(serializer.data)

# Create your views here.
