from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from chat.models import Message

def index(request):
    allMsg = Message.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'allMsg': allMsg,
    }
    return HttpResponse(template.render(context, request))