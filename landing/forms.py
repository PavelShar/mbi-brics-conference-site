from django import forms
from models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #
    #     if kwargs.get('instance'):
    #         email = kwargs['instance'].email
    #         kwargs.setdefault('initial', {})['confirm_email'] = email
    #
    #     return super(ContactForm, self).__init__(*args, **kwargs)