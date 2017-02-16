from django.shortcuts import render
from landing.models import *
from .forms import SubmissionForm
from django.contrib import messages


def index(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'areas' : Areas.objects.all(),
        'speakers' : Speakers.objects.all(),
        'topics' : TopicAreas.objects.all(),
        'dates' : ImportantDates.objects.all(),
        'footer' : Footer.objects.first(),
        'organizers' : Organizers.objects.order_by('?').all(),
        'publications' : Publications.objects.all()
    }
    return render(request, '2017/index.html', context)


def submission_form(request):

    context = {
        'base_info': BaseInfo.objects.first(),
        'footer': Footer.objects.first(),
        'form': SubmissionForm()
    }

    if request.method == 'POST':
        form = SubmissionForm(request.POST or None)
        if form.is_valid():
            form.save()
            render(request, '2017/submission/thanks.html')
        else:
            messages.error(request, "Error")

    return render(request, '2017/submission/form.html', context)