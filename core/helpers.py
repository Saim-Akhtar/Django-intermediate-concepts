from django.conf import settings
from django.core.mail import send_mail

def send_email(subject,message,email):
    from_email = settings.EMAIL_HOST_USER
    email_list = [email]
    send_mail(subject,message,from_email,email_list)