from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from landing.models import *
from .forms import SubmissionForm
from django.contrib import messages


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
    return render(request, '2017/index.html', context)


def submission_form(request):

    context = {
        'base_info': BaseInfo.objects.first(),
        'footer': Footer.objects.first(),
        'menus': Menu.objects.all(),
        'form': SubmissionForm()
    }

    if request.method == 'POST':
        form = SubmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('submission_success'))

    return render(request, '2017/submission/form.html', context)



def submission_success(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'menus': Menu.objects.all(),
        'footer': Footer.objects.first(),
    }

    return render(request, '2017/submission/thanks.html', context)