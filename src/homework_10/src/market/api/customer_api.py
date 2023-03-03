from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed, NotAcceptable
from rest_framework.response import Response

from ..shop.models.customer_model import Customer
from ..serializers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def partial_update(self, request, *args, **kwargs):
        allowed_fields = ['first_name', 'last_name', 'email']  # allowed fields to update

        if set(request.data.keys()) - set(allowed_fields):
            raise MethodNotAllowed('PATCH', 'Invalid fields')

        instance = self.get_object()

        user = instance.user
        for field in allowed_fields:
            if field in request.data:
                if field == "email":
                    email = request.data[field]
                    # Check if the email already exists in the User model
                    if User.objects.filter(username=email).exists():
                        raise NotAcceptable({'email': 'This email is already taken.'})

                    # Check if the new email is the same as the current email
                    if email == instance.user.username:
                        return Response(self.get_serializer(instance).data)

                    instance.user.username = email
                else:
                    setattr(user, field, request.data[field])
        user.save()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
