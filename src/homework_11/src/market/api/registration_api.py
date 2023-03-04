import json
from datetime import datetime

import jwt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from ..tools.jwt_tools import generate_jwt
from ..shop.models.user_verification_model import UserVerification
from ..shop.models.customer_model import Customer
from ..shop.models.store_owner_model import StoreOwner


class RegistrationView(View):

    @staticmethod
    def login(request):
        data = json.loads(request.body)

        try:
            email = data["email"]
            password = data["password"]
            print(password)

        except KeyError:
            return HttpResponseBadRequest("no data")

        user = authenticate(username=email, password=password)
        if user:

            login(request, user)
            jwt_token = generate_jwt(user)
            refresh_jwt_token = generate_jwt(user, True)
            response = JsonResponse({"access_token": jwt_token,
                                     "refresh_token": refresh_jwt_token})
            return response
        else:
            user = get_object_or_404(User, username=email)

            if not user.is_active:
                return HttpResponseBadRequest("User not verified")
            return HttpResponseBadRequest(f"{user} wrong password")

    @staticmethod
    def refresh_token(request):
        data = json.loads(request.body.decode("utf-8"))
        try:
            refresh_token = data["refresh_token"]
        except KeyError:
            return HttpResponseBadRequest("no data")

        try:
            jwt_payload = jwt.decode(refresh_token, "SECRET_KEY", algorithms=["HS256"])
            user_id = jwt_payload["user_id"]
            user = User.objects.get(id=user_id)

            # Check if the refresh token has expired
            refresh_token_exp = datetime.strptime(jwt_payload["expiration"], '%Y-%m-%d %H:%M:%S.%f')
            if datetime.utcnow() > refresh_token_exp:
                return HttpResponseBadRequest("refresh token expired")

            # Issue a new access token
            jwt_token = generate_jwt(user)

            return JsonResponse({"access_token": jwt_token.decode("utf-8")})

        except jwt.exceptions.DecodeError:
            return HttpResponseBadRequest("invalid token")

    @staticmethod
    def register(request):
        data = json.loads(request.body)
        try:
            password = data["password"]
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            is_owner = data["is_owner"]

        except ValueError:
            return JsonResponse({"message": "no_data"})

        if User.objects.filter(username=email).exists():
            return JsonResponse({"message": "already_exist"})

        user = User.objects.create_user(username=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        user.save()

        # create UserVerification object and generate verification code
        verification = UserVerification(user=user)
        verification.generate_verification_code()
        verification.send_verification_email()

        if not is_owner:
            Customer.objects.create(user=user)
            return JsonResponse({"message": "Customer created"})
        else:
            StoreOwner.objects.create(user=user)
            return JsonResponse({"message": "Store Owner created"})

    @staticmethod
    def logout(request):
        logout(request)
        return JsonResponse({"message": "logged out"})

    @staticmethod
    def send_verification_code(request, user_id):
        user = get_object_or_404(User, id=user_id)

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

        # Verify the user's email address.
        try:
            user = User.objects.get(username=email)
            verification = UserVerification.objects.filter(user=user, verification_code=verification_code).first()
            if verification:
                user.is_active = True
                user.save()
                return JsonResponse({"message": "User verified successfully"})
        except User.DoesNotExist:
            pass

        # Change the user's email address.
        try:
            old_email = request.GET.get('old_email')
            user = User.objects.get(username=old_email)
            verification = UserVerification.objects.get(user=user, verification_code=verification_code)
            user.username = email
            user.save()
            return JsonResponse({"message": "User email changed"})
        except (User.DoesNotExist, UserVerification.DoesNotExist):
            return HttpResponse("Invalid verification code", status=400)
