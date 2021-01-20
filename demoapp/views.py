from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from demoapp.authentication import MyAuthentication
from demoapp.serializer import UserModelSerializer


class UserDetailAPIVIew(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [MyAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({"username": request.user.username})


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):

        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "user": UserModelSerializer(serializer.obj).data,
            "token": serializer.token
        })
