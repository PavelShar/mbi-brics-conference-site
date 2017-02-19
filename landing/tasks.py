from celery.task import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@task(name="send_submission_success_email_task")
def send_submission_success_email_task(email):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent email")
    return send_mail(
        'Thank you for your submission!',
        '',
        'BRICS Global Business & Innovation Conference',
        [email],
        fail_silently=False,
    )