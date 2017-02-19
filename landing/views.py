from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from landing.models import *
from .forms import SubmissionForm


def index(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'menus' : Menu.objects.all(),
        'areas' : Areas.objects.all(),
        'news' : News.objects.filter(published=True).order_by('-date'),
        'speakers' : Speakers.objects.all(),
        'topics' : TopicAreas.objects.all(),
        'dates' : ImportantDates.objects.all(),
        'footer' : Footer.objects.first(),
        'prog_com' : Organizers.objects.filter(Q(committee__contains='prog')),
        'org_com': Organizers.objects.filter(Q(committee__contains='org')),
        'publications' : Publications.objects.all()
    }
    return render(request, '2017/pages/landing/index.html', context)


def submission_form(request):

    context = {
        'base_info': BaseInfo.objects.first(),
        'footer': Footer.objects.first(),
        'menus': Menu.objects.all(),
        'form': SubmissionForm()
    }

    baseInfo = BaseInfo.objects.values('submission_open').first()
    if baseInfo['submission_open'] == True:
        if request.method == 'POST':
            form = SubmissionForm(request.POST or None)
            if form.is_valid():
                form.save()


                # email = form['email'].value()
                # if len(email) > 0:

                    # send_mail(
                    #     'Thank you for your submission',
                    #     '',
                    #     'BRICS Conference Site',
                    #     [email],
                    #     fail_silently=False,
                    # )

                return HttpResponseRedirect(reverse('submission_success'))

        return render(request, '2017/pages/submission/form.html', context)
    else:
        return render(request, '2017/pages/submission/closed.html', context)


def submission_success(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'menus': Menu.objects.all(),
        'footer': Footer.objects.first(),
    }

    return render(request, '2017/pages/submission/thanks.html', context)



def submission_guidelines(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'menus': Menu.objects.all(),
        'footer': Footer.objects.first(),
        'guidelines' : SubmissionGuidelines.objects.all()
    }

    return render(request, '2017/pages/submission/guidelines.html', context)


def visa_steps(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'menus': Menu.objects.all(),
        'footer': Footer.objects.first(),
        'visa_steps' : VisaSteps.objects.all()
    }

    return render(request, '2017/pages/visa/visa.html', context)



def practical_info(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'menus': Menu.objects.all(),
        'footer': Footer.objects.first(),
        'practicals': Practical.objects.all()
    }

    return render(request, '2017/pages/practical/practical.html', context)