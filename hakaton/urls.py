from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from apps.tasks.urls import tasks_router
from apps.users.urls import users_router


router = routers.DefaultRouter()
router.registry.extend(tasks_router.registry)
router.registry.extend(users_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('api/users/', include('apps.users.urls')),  # Подключаем urls пользователей
]
