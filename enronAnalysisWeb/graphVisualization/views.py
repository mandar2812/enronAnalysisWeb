from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World!!')
