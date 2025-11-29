from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializer import TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer