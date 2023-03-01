import json
from datetime import datetime

import jwt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth import logout, login, authenticate

from ..tools.jwt_tools import generate_jwt
from ..tools.sending_tools import data_status, ok_status
from ..shop.models.user_model import CustomUser


class RegistrationView(View):

    @staticmethod
    def login(request):
        data = json.loads(request.body.decode("utf-8"))

        try:
            email = data["email"]
            password = data["password"]

        except KeyError:
            return HttpResponse("no data")

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            jwt_token = generate_jwt(user)
            refresh_jwt_token = generate_jwt(user, True)
            response = JsonResponse({"access_token": jwt_token,
                                     "refresh_token": refresh_jwt_token})
            return response
        else:
            try:
                user = CustomUser.objects.get(username=email)
            except ObjectDoesNotExist:
                return HttpResponse("invalid login credentials")
            return HttpResponse(f"{user} wrong password")

    @staticmethod
    def refresh_token(request):
        data = json.loads(request.body.decode("utf-8"))
        try:
            refresh_token = data["refresh_token"]
        except KeyError:
            return HttpResponse("no data")

        try:
            jwt_payload = jwt.decode(refresh_token, "SECRET_KEY", algorithms=["HS256"])
            user_id = jwt_payload["user_id"]
            user = CustomUser.objects.get(id=user_id)

            # Check if the refresh token has expired
            refresh_token_exp = datetime.strptime(jwt_payload["expiration"], '%Y-%m-%d %H:%M:%S.%f')
            if datetime.utcnow() > refresh_token_exp:
                return HttpResponse("refresh token expired")

            # Issue a new access token
            jwt_token = generate_jwt(user)

            return JsonResponse({"access_token": jwt_token.decode("utf-8")})

        except jwt.exceptions.DecodeError:
            return HttpResponse("invalid token")

    @staticmethod
    def register(request):
        data = json.loads(request.body)
        try:
            password = data["password"]
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]

        except ValueError:
            return json.dumps(({"no_data"}))

        if CustomUser.objects.filter(username=email).exists():
            return json.dumps(({"already_exist"}))

        user = CustomUser.objects.create_user(username=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return JsonResponse({"message": "user created"})

    @staticmethod
    def logout(request):
        logout(request)
        return JsonResponse({"message": "logged out"})
