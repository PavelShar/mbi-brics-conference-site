from django.http import HttpResponse
from django.shortcuts import render

from landing.models import *


def index(request):
    context = {
        'base_info': BaseInfo.objects.first(),
        'areas' : Areas.objects.all(),
        'speakers' : Speakers.objects.all(),
        'topics' : TopicAreas.objects.all(),
        'dates' : ImportantDates.objects.all(),
        'footer' : Footer.objects.first(),
        'organizers' : Organizers.objects.order_by('?').all(),
    }
    return render(request, 'index.html', context)
