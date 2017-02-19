from captcha.fields import ReCaptchaField
from django import forms
from models import Submission
from tasks import *


class SubmissionForm(forms.ModelForm):
    captcha = ReCaptchaField(label='',attrs={
        'theme': 'clean',
        'callback' : 'verifyCallback'
    })

    def send_email_success_sync(self):
        send_mail('Thank you for your submission', '', 'BRICS Global Business & Innovation Conference', [self.cleaned_data['email']], fail_silently=False, )

    def send_email_success_async(self):
        send_submission_success_email_task.delay(self.cleaned_data['email'])

    class Meta:
        model = Submission
        exclude = ('created_at',)
