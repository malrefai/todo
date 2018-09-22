from rest_framework import viewsets

from app.models.todo import Todo
from app.serializers.todo_serializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve` and `destroy` actions
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
