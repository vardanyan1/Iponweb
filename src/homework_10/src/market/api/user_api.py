import json

from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers.auth_serializers import (RegisterSerializer, VerificationSerializer, ChangePasswordSerializer)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        is_owner = data["is_owner"]
        serializer = self.get_serializer(data=request.data, context={'is_owner': is_owner})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VerificationView(APIView):
    def get(self, request):
        serializer = VerificationSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = {"message": "User verified successfully"}
        return Response(response_data, status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
