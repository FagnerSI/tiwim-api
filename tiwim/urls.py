from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from project.views import ProjectView
from role.views import RoleView
from topic.views import TopicView
from replay.views import ReplayView
from account.views import AccountView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'roles', RoleView)
router.register(r'projects', ProjectView)
router.register(r'topics', TopicView)
router.register(r'replays', ReplayView)
router.register(r'accounts', AccountView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
