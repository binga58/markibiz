from django.utils import timezone
import datetime
from django.shortcuts import render,HttpResponseRedirect
from .forms import FeedbackForm
from .models import Event, Team,User
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date


@csrf_exempt
def home(request):
    object = Event.objects.all()
    present = []
    past = []
    upcoming = []
    for ob in object:
        if ob.registration_start > timezone.now():
            upcoming.append(ob)
        elif ob.event_end < timezone.now():
            past.append(ob)
        else:
            present.append(ob)
    context = {
        "present":present,
        "upcoming":upcoming,
        "past":past,
    }
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = User(name = name, email_id = email)
        user.save()
        return HttpResponseRedirect('')

    else:
        return render(request,'home.html', context)

def feedback(request):
    form = FeedbackForm(request.POST or None)
    context = {"form":form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return (request,'home.html',{})


    return render(request,'feedback.html',context)

def team(request):
    object = Team.objects.all().order_by("-level")
    context = {
        "object":object

    }
    return render(request,'team.html',context)


def event(request, id):

    object = Event.objects.get(pk=id)


    now = timezone.now()

    context = {
        "object":object,
        'now':now,
    }
    return render(request,'event.html',context)


def list(request):
    object = Event.objects.all()
    present = []
    past = []
    upcoming = []
    for ob in object:
        if ob.registration_start > timezone.now():
            upcoming.append(ob)
        elif ob.event_end < timezone.now():
            past.append(ob)
        else:
            present.append(ob)


    context = {
        "present":present,
        "upcoming":upcoming,
        "past":past,
    }
    return render(request,'list.html',context)



def markquest(request):
    context = {

    }
    return  render(request,'description.html',context)
