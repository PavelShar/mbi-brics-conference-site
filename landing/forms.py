from captcha.fields import ReCaptchaField
from django import forms
from django.template.loader import render_to_string

from models import Submission
from tasks import *


class SubmissionForm(forms.ModelForm):
    captcha = ReCaptchaField(label='', attrs={
        'theme': 'clean',
        'callback': 'verifyCallback'
    })


    def send_email_success_sync(self):
        send_mail( settings.EMAIL_TITLE_TEMPLATE, '', settings.DEFAULT_EMAIL_FROM, [self.cleaned_data['email']], fail_silently=False, html_message=self.create_email_template())

    def send_email_success_async(self):
        send_submission_success_email_task.delay(self.cleaned_data['email'], self.create_email_template())


    def create_email_template(self):
        return render_to_string('2017/components/email.html', {'name': self.cleaned_data['first_name']})

    class Meta:
        model = Submission
        exclude = ('created_at',)
