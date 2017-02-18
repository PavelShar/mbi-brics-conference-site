from captcha.fields import ReCaptchaField
from django import forms
from models import Submission


class SubmissionForm(forms.ModelForm):
    captcha = ReCaptchaField(label='',attrs={
        'theme': 'clean',
        'callback' : 'verifyCallback'
    })
    class Meta:
        model = Submission
        #fields = '__all__',
        exclude = ('created_at',)
