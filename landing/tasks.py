from celery.task import task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@task(name="send_submission_success_email_task")
def send_submission_success_email_task(email, body):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent email")
    return send_mail(
        settings.EMAIL_TITLE_TEMPLATE,
        '',
        settings.DEFAULT_EMAIL_FROM,
        [email],
        fail_silently=False, html_message=body
    )