__author__ = 'imran'

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader

from django.shortcuts import render, get_object_or_404

def index(request):

    return HttpResponseRedirect('/telephony/')
