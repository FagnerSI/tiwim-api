from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from user.views import UserView
from project.views import ProjectView
from role.views import RoleView
from topic.views import TopicView
from replay.views import ReplayView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView)
router.register(r'roles', RoleView)
router.register(r'projects', ProjectView)
router.register(r'topics', TopicView)
router.register(r'replays', ReplayView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('v1/api-token/', obtain_auth_token)
]
