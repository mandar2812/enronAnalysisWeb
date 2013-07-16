from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response

def index():
    print '<html><body><h1>Hello World!!<h1></body></html>>'
