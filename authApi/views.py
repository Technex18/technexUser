from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
import requests
from django.views.decorators.csrf import csrf_exempt
import json
import os
import facebook
from Auth.models import *
#from Auth.forms import *
# Create your views here.
def contextCall(request):
    response = {}
    try:
        user = request.user
        techprofile = user.techprofile
        response['user'] = user
        response['techProfile'] = techprofile
    except:
        pass
    return response

@csrf_exempt
def ApiRegisterView(request):
    response = {}
    try:
        data =json.loads(request.body)
        #form = RegisterForm(data)
        email = data.get('email',None)
        try:
            user = User.objects.get(email = email)
            response['status'] = 2 #for already registered
            return JsonResponse(response)
        except:
        	user = User.objects.create_user(username=email, email=email)
        user.first_name = data.get('name',None)
        password = data.get('password',None)
        user.set_password(password)
        user.save()
        try:
            college = College.objects.get(collegeName = data.get('college'))
        except:
            college = College(collegeName = data.get('college'))
            college.save()
        try:
        	techprofile = TechProfile.objects.get(user = user)
        except:
			techprofile = TechProfile(user = user)
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.year = data.get('year')
        techprofile.save()
		#print "codeBaes 2"

        newUser = authenticate(username=email, password=password)
        login(request, newUser)
        response['name'] = newUser.first_name
        response['mobileNumber'] = techprofile.mobileNumber
        response['year'] = techprofile.year
        response['college'] = techprofile.college.collegeName
        response['email'] = newUser.email
        response['status'] = 1
        return JsonResponse(response)
    except:
        response['status'] = 0 #For unknown error
        return JsonResponse(response)

@csrf_exempt
def ApiLoginView(request):
    response_data = {}
    try:
        data = json.loads(request.body)
        #form = LoginForm(data)
        
        email = data.get('email',None)
        password = data.get('password',None)
        user = authenticate(username=email, email=email, password=password)
        if user is not None:
            login(request, user)
            response_data['status'] = 1
            response_data['name'] = user.first_name
            response_data['email'] = user.email
            techprofile = TechProfile.objects.get(user = user)
            response_data['mobileNumber'] = techprofile.mobileNumber
            response_data['year'] = techprofile.year
            response_data['college'] = techprofile.college.collegeName
            return JsonResponse(response_data)
        else:
            response_data['status'] = 0 #Invalid credentials
            return JsonResponse(response_data)
    except:
        response_data['status'] = 2 #email field not filled correctly
        return JsonResponse(response_data)

@csrf_exempt
@login_required(login_url='/api/eventApi') #not /login/
def logoutApi(request):
    logout(request)
    response = {}
    response['status'] = "logged Out"
    return JsonResponse(response)

@csrf_exempt
def eventApi(request):
    response = {}
    try:
        parentEvents = ParentEvent.objects.all()
        response['data'] = []
        for parentEvent in parentEvents:
            pEventData = {}
            pEventData['name'] = parentEvent.categoryName
            pEventData['description'] = parentEvent.description
            pEventData['order'] = parentEvent.order
            pEventData['events'] = []
            events = Event.objects.filter(parentEvent = parentEvent)
            for event in events:
                eventData = {}
                eventData['eventName'] = event.eventName
                eventData['description'] = event.description
                eventData['deadLine'] = event.deadLine
                eventData['prizeMoney'] = event.prizeMoney
                eventData['maxMembers'] = event.maxMembers
                eventData['eventOrder'] = event.eventOrder
                eventData['eventOptions'] = []
                eventOptions = EventOption.objects.filter(event = event)
                for eventOption in eventOptions:
                    eventOptionData = {}
                    eventOptionData['optionName'] = eventOption.optionName
                    eventOptionData['optionDescription'] = eventOption.optionDescription
                    eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                    eventData['eventOptions'].append(eventOptionData)
                pEventData['events'].append(eventData)
            response['data'].append(pEventData)
            response['status'] = 1
        return JsonResponse(response)
    except:
        response['error'] = True
        response['status'] = 'Error in finding events'
        return JsonResponse(response)

@csrf_exempt
def eventData(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        slug = data['parentEvent']
        try:
            parentEvent = ParentEvent.objects.get(nameSlug = slug)
        except:
            response['error'] = True
            response['status'] = 'Invalid Slug for Parent Event'
            return JsonResponse(response)
        response['name'] = parentEvent.categoryName
        response['description'] = parentEvent.description
        response['order'] = parentEvent.order
        response['events'] = []
        events = Event.objects.filter(parentEvent = parentEvent)
        for event in events:
            eventData = {}
            eventData['eventName'] = event.eventName
            eventData['description'] = event.description
            eventData['deadLine'] = event.deadLine
            eventData['prizeMoney'] = event.prizeMoney
            eventData['maxMembers'] = event.maxMembers
            eventData['eventOrder'] = event.eventOrder
            eventData['eventOptions'] = []
            eventOptions = EventOption.objects.filter(event = event)
            for eventOption in eventOptions:
                eventOptionData = {}
                eventOptionData['optionName'] = eventOption.optionName
                eventOptionData['optionDescription'] = eventOption.optionDescription
                eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                eventData['eventOptions'].append(eventOptionData)
            response['events'].append(eventData)
        
        return JsonResponse(response)
    else:
        response['error'] = True
        response['status'] = 'Invalid Request'
        return JsonResponse(response)

@csrf_exempt
def parentEvents(request):
    response = {}
    if True:
        parentEvents = ParentEvent.objects.all()
        response['data'] = []
        for parentEvent in parentEvents:
            pEventData = {}
            pEventData['name'] = parentEvent.categoryName
            pEventData['description'] = parentEvent.description
            pEventData['order'] = parentEvent.order
            response['data'].append(pEventData)
        return JsonResponse(response)
    else:
        response['error'] = True
        response['status'] = 'Error getting Data!'
        return JsonResponse(response)