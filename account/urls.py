from django.conf.urls import url
from django.urls import include, path

from .views import (
    AccountView,
)

urlpatterns = [
    path('register/', AccountView.as_view(), name='account-register'),

]

"""   path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user-logout'),
    path('<slug:username>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('<slug:username>/edit/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<slug:username>/delete/',
         UserDeleteAPIView.as_view(), name='user-delete'), """
