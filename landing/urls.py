from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^2017/$', views.index, name='index'),
    url(r'^brics/$', views.index, name='index'),
    url(r'^brics/submit/$', views.submission_form, name='submission_form'),
    url(r'^brics/submit/success/$', views.submission_success, name='submission_success'),
    url(r'^brics/visa/$', views.visa_steps, name='visa_steps'),
    url(r'^brics/practical/$', views.practical_info, name='practical_info'),
]