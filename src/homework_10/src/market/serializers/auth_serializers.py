from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..shop.models.customer_model import Customer
from ..shop.models.store_owner_model import StoreOwner
from ..shop.models.user_verification_model import UserVerification


class VerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField()

    def validate(self, data):
        email = data['email']
        verification_code = data['verification_code']

        try:
            user = User.objects.get(username=email)
            verification = UserVerification.objects.filter(user=user, verification_code=verification_code).first()

            if not verification:
                raise serializers.ValidationError("Invalid verification code")

            if user.is_active:
                raise serializers.ValidationError("User has already been verified")

            data['user'] = user

        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email address")

        return data

    def save(self, **kwargs):
        user = self.validated_data['user']
        user.is_active = True
        user.save()

        return user


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        verification = UserVerification(user=user)
        verification.generate_verification_code()
        verification.send_verification_email()

        if 'is_owner' in self.context and self.context['is_owner']:
            StoreOwner.objects.create(user=user)
            return user
        elif 'is_owner' in self.context and not self.context['is_owner']:
            Customer.objects.create(user=user)
            return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
