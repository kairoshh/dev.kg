# from django.core.mail import EmailMessage
# from django.conf import settings

# def send_msg(email):
#     mail = EmailMessage(
#         'Message title',
#         'Приветсвуем на нашем сайте!',
#         settings.EMAIL_HOST_USER,
#         [email]
        
#     )
#     mail.send()

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.auth import get_user_model
from celery import shared_task

User = get_user_model()

@shared_task
def send_msg(email):
    user = User.objects.filter(email=email).last()

    context = {
        'username': user.username
    }

    html_message = render_to_string('index.html', context)

    mail.send_mail(
        'Hi it`s title',
        strip_tags(html_message), settings.EMAIL_HOST_USER,
        [email], html_message=html_message
    )