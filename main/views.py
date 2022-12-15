import json 
from django.shortcuts import render
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from main.models import CybersafeModel


# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def about(request):
    pass

def shithead(request):
    pass


@csrf_exempt
def cybersafe(request):
    res = json.loads(request.body)
    email= res['email']
    message =res['message']
    subject = res['subject']
    if CybersafeModel.objects.filter(email=email).exists() and CybersafeModel.objects.filter(message=message).exists():
        return JsonResponse({"status":"alreadysent"})
    else:
        newm = CybersafeModel(email=email,message=message,subject=subject)
        newm.save()
        message2 = "MESSAGE:= " + message +"\n REPLY TO:=  " + email
        send_mail(
            subject,
            message2,
            'contact@cybersafecal.com',
            ['contact@cybersafecal.com'],
             fail_silently=False,
            )
            
           
        return JsonResponse({"status":"success"})
    