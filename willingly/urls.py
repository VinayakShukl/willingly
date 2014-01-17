from django.conf.urls import *
from core.views import home

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template',{'template': 'home.html'}),
    url(r'^$', home),
)
