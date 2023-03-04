from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.exceptions import MethodNotAllowed, NotAcceptable
from rest_framework.response import Response

from ..shop.models.customer_model import Customer
from ..serializers.serializers import CustomerSerializer
from ..shop.models.user_verification_model import UserVerification


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    allowed_fields = ['first_name', 'last_name', 'email']  # allowed fields to update

    def create(self, request, *args, **kwargs):
        user_data = {
            'username': request.data['email'],
            'password': request.data['password'],
            'email': request.data['email']
        }

        # Add first_name and last_name to user_data if present in request.data
        if 'first_name' in request.data:
            user_data['first_name'] = request.data['first_name']
        if 'last_name' in request.data:
            user_data['last_name'] = request.data['last_name']

        user = User.objects.create_user(**user_data)
        user.is_active = False
        user.save()

        # create UserVerification object and generate verification code
        verification = UserVerification(user=user)
        verification.generate_verification_code()
        verification.send_verification_email()

        customer_data = {
            'user': user.id
        }
        serializer = self.get_serializer(data=customer_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        invalid_fields = set(request.data.keys()) - set(self.allowed_fields)
        if invalid_fields:
            raise MethodNotAllowed('PATCH', f"Invalid fields: {', '.join(invalid_fields)}")

        instance = self.get_object()
        user = instance.user

        for field in self.allowed_fields:
            if field in request.data:
                if field == "email":
                    self.update_email(instance, request.data[field])
                else:
                    setattr(user, field, request.data[field])

        user.save()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def update_email(self, instance, email):
        if email == instance.user.username:
            return

        if User.objects.filter(username=email).exists():
            raise NotAcceptable({'email': 'This email is already taken.'})

        verification = UserVerification.objects.get(user=instance.user)
        verification.generate_verification_code()
        verification.send_verification_email(new_email=email)
