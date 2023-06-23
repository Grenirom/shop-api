from django.core.mail import send_mail

HOST = '127.0.0.1:8000'


def send_confirmation_email(user, code):
    link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    send_mail(
        'Hello, activate your account!',
        f'To activate your account, click the link below:'
        f'\n{link}'
        f'\nThe link is for one-time use!)',
        'ngrebnev17@gmail.com',
        [user],
        fail_silently=False,
    )

