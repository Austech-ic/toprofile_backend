#when a user is created a signal otp is been sent out to the user

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
import string
from .models import EmailVerification
from .helpers import send_emails

# smart_bytes convert your uid to byte and urlsafe_base64 convert to save string


@receiver(post_save, sender=settings.AUTH_USER_MODEL, dispatch_uid="unique_identifier")
def send_otp_to_email(sender, instance, created, **kwargs):
    if created:
        try:
            send_emails(instance.email)
        #     otp=get_random_string(5,allowed_chars=string.digits)
        #     subject = 'Confirm Your Email Address'
        #     message = render_to_string('accounts/email_confirmation.html', {
        #     "otp":otp
        # })
        #     from_email = settings.EMAIL_HOST_USER
        #     to_email = instance.email
        #     send_mail(subject, message, from_email, [to_email], fail_silently=False)
        #     #save the email and the otp to email verification table
        #     EmailVerification.objects.create(email=instance.email,otp=otp)
        except Exception as e:
            print(f'Error sending confirmation email: {e}')
