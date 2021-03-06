from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'sprints', views.SprintViewSet)
router.register(r'task', views.TaskViewSet)
router.register(r'user', views.UserViewSet)