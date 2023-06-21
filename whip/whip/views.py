import os
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import whip_api_to_get,whip_api_output

def whip_gestational_limits_API(request):
    refreshme = whip_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = whip_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = whip_api_to_get(whip_api = "https://api.abortionpolicyapi.com/v1/gestational_limits/states/")
    savecommand.save()    
    os.system('python3 whipAPI.py')
    latest_answer = whip_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/whip_answer.html', latest_proposed_dict)

def whip_insurance_coverage_API(request):
    refreshme = whip_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = whip_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = whip_api_to_get(whip_api = "https://api.abortionpolicyapi.com/v1/insurance_coverage/states/")
    savecommand.save()    
    os.system('python3 whipAPI.py')
    latest_answer = whip_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/whip_answer.html', latest_proposed_dict)

def whip_minors_API(request):
    refreshme = whip_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = whip_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = whip_api_to_get(whip_api = "https://api.abortionpolicyapi.com/v1/minors/states/")
    savecommand.save()    
    os.system('python3 whipAPI.py')
    latest_answer = whip_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/whip_answer.html', latest_proposed_dict)

def whip_waiting_period_API(request):
    refreshme = whip_api_output.objects.all()
    refreshme.delete()
    refreshmetoo = whip_api_to_get.objects.all()
    refreshmetoo.delete()    
    savecommand = whip_api_to_get(whip_api = "https://api.abortionpolicyapi.com/v1/waiting_periods/states/")
    savecommand.save()    
    os.system('python3 whipAPI.py')
    latest_answer = whip_api_output.objects.all()
    latest_proposed_dict = {
        'latest_proposed_dict': latest_answer
    }
    return render(request, 'Answer/whip_answer.html', latest_proposed_dict)