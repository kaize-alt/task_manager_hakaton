from rest_framework import routers
from .views import (
    BoardViewSet, TableViewSet, TaskViewSet, TaskUpdateViewSet,
    TaskDeleteViewSet, CommentViewSet
)

tasks_router = routers.DefaultRouter()

tasks_router.register(r"boards", BoardViewSet, basename="boards")
tasks_router.register(r"tables", TableViewSet, basename="tables")
tasks_router.register(r"tasks", TaskViewSet, basename="tasks")
tasks_router.register(r"tasks/update", TaskUpdateViewSet, basename="task-update")
tasks_router.register(r"tasks/delete", TaskDeleteViewSet, basename="task-delete")
tasks_router.register(r"comments", CommentViewSet, basename="comments")
