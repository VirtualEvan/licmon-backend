from flask import current_app, render_template, url_for

from licmon.vendor.django_mail import get_connection
from licmon.vendor.django_mail.message import EmailMultiAlternatives


def create_email(recipient_email, subject, text_template, html_template, context):
    text_content = render_template(text_template, **context)
    html_content = render_template(html_template, **context)
    noreply_address = current_app.config['NOREPLY_ADDRESS']
    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_email=noreply_address,
        to=[recipient_email],
    )
    msg.attach_alternative(html_content, 'text/html')
    return msg


def send_emails(emails):
    with get_connection() as conn:
        return conn.send_messages(emails)


def send_email(
    subject,
    text_template,
    html_template,
    context,
    users=None,
):
    if not users:
        return 0
    emails = [
        create_email(
            user_email,
            subject,
            text_template,
            html_template,
            context,
        )
        for user_email in ['epuentes@cern.ch']  # users
    ]
    return send_emails(emails)
