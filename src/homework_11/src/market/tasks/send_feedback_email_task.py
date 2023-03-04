from time import sleep
from django.core.mail import send_mail
from ..celery import app
from celery import shared_task

"""
To install and run flower need activate celery like: python3 -m celery -A market worker -l info  
After that in another terminal run: celery --broker=redis://localhost:6379 flower
"""


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""

    sleep(20)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email_address],
        fail_silently=False,
    )
