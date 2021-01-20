from django.urls import path
from rest_framework_jwt import views as view

from demoapp import views

urlpatterns = [
    path("login/", view.ObtainJSONWebToken.as_view()),
    # path("login/", view.obtain_jwt_token),
    path("users/", views.UserDetailAPIVIew.as_view()),
    path("user/", views.LoginAPIView.as_view()),
]
