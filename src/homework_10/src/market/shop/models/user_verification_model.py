from django.db import models
from django.contrib.auth.models import User

import random
import string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

import environ

env = environ.Env()
environ.Env.read_env()


class UserVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def generate_verification_code(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        self.verification_code = code
        self.save()
        return code

    def generate_verification_link(self):
        domain = env("DOMAIN")
        url = f"{domain}/api/auth/verify/?email={self.user.username}&code={self.verification_code}"
        return url

    def send_verification_email(self):
        subject = 'Confirm your email address'
        verification_link = self.generate_verification_link()

        html_message = render_to_string('verification_email.html', {'verification_code': verification_link})
        plain_message = strip_tags(html_message)
        from_email = env("GMAIL")
        to_email = self.user.username
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
