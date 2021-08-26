from django.urls import path
from Users.api.views.user_views import *

urlpatterns = [
    path("create-user/", CreateUser.as_view(), name='create-user'),
    path("login/", Login.as_view(), name='login'),
    path("connected/", Connected.as_view(), name='connected'),
    path("logout/", Logout.as_view(), name='logout'),


]