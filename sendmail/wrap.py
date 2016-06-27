from django.conf import settings

from channels import Channel


def get_channel_name():
    return getattr(settings, 'CHANNELS_SENDMAIL_CHANNEL_NAME', 'django.core.mail.send_mail')


def send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None):

    message = dict(
        subject = subject,
        message = message,
        from_email = from_email,
        recipient_list = recipient_list,
        fail_silently = fail_silently,
        auth_user = auth_user,
        auth_password = auth_password,
        connection = connection,
        html_message = html_message,
    )

    channel_name = get_channel_name()
    Channel(channel_name).send(message)
