from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('graphVisualization/starter-template.html')
    context = RequestContext(request, {
        'latest_poll_list' : ['Mandar', 'Aniket', 'Subhendu']
    })
    return HttpResponse(template.render(context))
