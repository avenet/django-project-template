# -*- coding: utf-8 -*-
""" This file contains some generic purpouse views """

# standard library
import json

# django
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def index(request):
    """ view that renders a default home"""
    return render_to_response('index.jade',
                              context_instance=RequestContext(request))


def bad_request_view(request):
    return render_to_response('exceptions/400.jade', {},
                              context_instance=RequestContext(request))


def permission_denied_view(request):
    return render_to_response('exceptions/403.jade', {},
                              context_instance=RequestContext(request))


def page_not_found_view(request):
    return render_to_response('exceptions/404.jade', {},
                              context_instance=RequestContext(request))


def error_view(request):
    return render_to_response('exceptions/500.jade', {},
                              context_instance=RequestContext(request))


def json_view(request, response=None):
    if response is None:
        response = {}

    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder),
                        content_type="application/json")
