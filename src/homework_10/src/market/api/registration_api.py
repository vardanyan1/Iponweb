import json
from datetime import datetime

import jwt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from ..tools.jwt_tools import generate_jwt
from ..tools.sending_tools import data_status, ok_status
from ..shop.models.user_verification_model import UserVerification


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

            if not user.is_active:
                return HttpResponse("User not verified", status=400)

            login(request, user)
            jwt_token = generate_jwt(user)
            refresh_jwt_token = generate_jwt(user, True)
            response = JsonResponse({"access_token": jwt_token,
                                     "refresh_token": refresh_jwt_token})
            return response
        else:
            try:
                user = User.objects.get(username=email)
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
            user = User.objects.get(id=user_id)

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
            return JsonResponse(json.dumps(({"no_data"})))

        if User.objects.filter(username=email).exists():
            return JsonResponse(json.dumps(({"already_exist"})))

        user = User.objects.create_user(username=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        user.save()

        # create UserVerification object and generate verification code
        verification = UserVerification(user=user)
        verification.generate_verification_code()

        # send verification email
        verification.send_verification_email()

        return JsonResponse({"message": "user created"})

    @staticmethod
    def logout(request):
        logout(request)
        return JsonResponse({"message": "logged out"})

    @staticmethod
    def send_verification_code(request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return HttpResponse("User not found", status=404)

        verification = UserVerification(user=user)
        verification_code = verification.generate_verification_code()
        verification.send_verification_email()

        verification.save()
        return JsonResponse({"message": "Verification email sent"})

    @staticmethod
    def verify(request):
        email = request.GET.get('email')
        verification_code = request.GET.get('code')

        if not email or not verification_code:
            return HttpResponse("Invalid verification link", status=400)

        try:
            user = User.objects.get(username=email)
            verification = UserVerification.objects.get(user=user, verification_code=verification_code)
        except (User.DoesNotExist, UserVerification.DoesNotExist):
            return HttpResponse("Invalid verification code", status=400)

        user.is_active = True
        user.save()

        return JsonResponse({"message": "User verified successfully"})
