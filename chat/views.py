from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from chat.models import Message

def index(request):
    allMsg = Message.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'allMsg': allMsg[::-1],
    }
    return HttpResponse(template.render(context, request))

def send(request, message):
    message.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse(''))