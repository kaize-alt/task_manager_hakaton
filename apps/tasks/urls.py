from rest_framework import routers
from .views import (
    BoardViewSet, BoardCreateViewSet, BoardUpdateViewSet, BoardDeleteViewSet,
    TableViewSet, TableCreateViewSet, TableUpdateViewSet, TableDeleteViewSet,
    TaskViewSet, TaskUpdateViewSet, TaskDeleteViewSet,
    CommentViewSet, CommentUpdateViewSet
)


tasks_router = routers.DefaultRouter()

tasks_router.register(r"boards", BoardViewSet, basename="boards")
tasks_router.register(r"boards/create", BoardCreateViewSet, basename="board-create")
tasks_router.register(r"boards/update", BoardUpdateViewSet, basename="board-update")
tasks_router.register(r"boards/delete", BoardDeleteViewSet, basename="board-delete")

tasks_router.register(r"tables", TableViewSet, basename="tables")
tasks_router.register(r"tables/create", TableCreateViewSet, basename="table-create")
tasks_router.register(r"tables/update", TableUpdateViewSet, basename="table-update")
tasks_router.register(r"tables/delete", TableDeleteViewSet, basename="table-delete")

tasks_router.register(r"tasks", TaskViewSet, basename="tasks")
tasks_router.register(r"tasks/update", TaskUpdateViewSet, basename="task-update")
tasks_router.register(r"tasks/delete", TaskDeleteViewSet, basename="task-delete")

tasks_router.register(r"comments", CommentViewSet, basename="comments")
tasks_router.register(r"comments/update", CommentUpdateViewSet, basename="comment-update")
