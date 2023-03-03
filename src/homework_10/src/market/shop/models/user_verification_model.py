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

    def generate_verification_link(self, email=None, old_email=None):
        domain = env("DOMAIN")
        if email and old_email:
            url = f"{domain}/api/auth/verify/?email={email}&old_email={old_email}&code={self.verification_code}"
        elif email:
            url = f"{domain}/api/auth/verify/?email={email}&code={self.verification_code}"
        else:
            raise ValueError("Either 'email' or 'old_email' must be provided.")
        return url

    def send_verification_email(self, new_email=None):
        if not new_email:
            verification_link = self.generate_verification_link(email=self.user.username)
            to_email = self.user.username
            subject = 'Confirm your email address'
        else:
            verification_link = self.generate_verification_link(email=new_email, old_email=self.user.username)
            to_email = new_email
            subject = 'Confirm your new email address'

        html_message = render_to_string('verification_email.html', {'verification_code': verification_link})
        plain_message = strip_tags(html_message)
        from_email = env("GMAIL")
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
