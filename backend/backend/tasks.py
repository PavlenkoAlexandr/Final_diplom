import logging

from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth import get_user_model

from backend import settings
from backend.celery import app


@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        msg = EmailMultiAlternatives(
            f'Verify your QuickPublisher account',
            'Follow this link to verify your account: '
            f'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email]
        )
        msg.send()
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)