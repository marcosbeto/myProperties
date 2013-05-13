# Create your views here.

from django.template.context import RequestContext
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponsePermanentRedirect, Http404

def goToURLControlPanel(request):
    return render_to_response('myPropertiesBase.html',{} , context_instance=RequestContext(request))

def goToURLLanding(request):
    return render_to_response('myPropertiesLanding.html',{} , context_instance=RequestContext(request))