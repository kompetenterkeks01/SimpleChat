from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from chat.models import Message

def index(request):
    allMsg = Message.objects.order_by('-id')
    template = loader.get_template('index.html')
    context = {
        'allMsg': allMsg[::-1],
    }
    return HttpResponse(template.render(context, request))

def send(request):
    uname = request.POST['name']
    msg = request.POST['msg']
    newMsg = Message()
    newMsg.msg = msg
    newMsg.user_name = uname
    newMsg.pub_date = timezone.now()
    newMsg.save()

    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect('/')