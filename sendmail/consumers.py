from django.core.mail import send_mail


def handle_send_mail(message):
    send_mail(
        message['subject'],
        message['message'],
        message['from_email'],
        message['recipient_list'],
        message['fail_silently'],
        message['auth_user'],
        message['auth_password'],
        message['connection'],
        message['html_message'],
    )
