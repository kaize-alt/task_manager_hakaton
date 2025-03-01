from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import mixins, viewsets, status

from .models import Board, Table, Task, Comment
from .serializers import (
    BoardSerializer, BoardCreateSerializer, BoardUpdateSerializer,
    TableSerializer, TableCreateSerializer, TableUpdateSerializer,
    TaskSerializer, TaskListSerializer, TaskUpdateSerializer,
    CommentSerializer, CommentUpdateSerializer
)


class BoardViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer
    def get_serializer_class(self ):
        if self.action == 'create':
            return BoardCreateSerializer
        return BoardSerializer

class BoardUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardUpdateSerializer


class BoardDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def destroy(self, request, *args, **kwargs):
        board_id = kwargs.get("pk")
        try:
            board = Board.objects.get(id=board_id)
            board.delete()
            return Response({"success": "Доска удалена"}, status=status.HTTP_200_OK)
        except Board.DoesNotExist:
            return Response({"error": "Доска не найдена"}, status=status.HTTP_404_NOT_FOUND)


class TableViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["board"]


class TableCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableCreateSerializer


class TableUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableUpdateSerializer


class TableDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def destroy(self, request, *args, **kwargs):
        table_id = kwargs.get("pk")
        try:
            table = Table.objects.get(id=table_id)
            table.delete()
            return Response({"success": "Таблица удалена"}, status=status.HTTP_200_OK)
        except Table.DoesNotExist:
            return Response({"error": "Таблица не найдена"}, status=status.HTTP_404_NOT_FOUND)


class TaskViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["table", "status", "assigned_to"]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["author"] = request.user.id

        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)


class TaskUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer


class TaskDeleteViewSet(mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        task_id = kwargs.get("pk")
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({"success": "Задача удалена"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Задача не найдена"}, status=status.HTTP_404_NOT_FOUND)


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.request.query_params.get("task")
        if not task_id:
            raise NotFound("Укажите task в параметрах запроса.")

        return Comment.objects.filter(task_id=task_id)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = request.user.id

        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()

        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


class CommentUpdateViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
