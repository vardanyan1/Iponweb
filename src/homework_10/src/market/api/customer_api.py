from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed, NotAcceptable
from rest_framework.response import Response

from ..shop.models.customer_model import Customer
from ..serializers.serializers import CustomerSerializer
from ..shop.models.user_verification_model import UserVerification


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    allowed_fields = ['first_name', 'last_name', 'email']  # allowed fields to update

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
