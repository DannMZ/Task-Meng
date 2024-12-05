from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet

# Налаштування маршрутизатора
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# URL-патерни
urlpatterns = [
    path('admin/', admin.site.urls),  # Адмінка
    path('api/', include(router.urls)),  # API
    path('', include('tasks.urls')),  # Підключення URL із додатку tasks
]