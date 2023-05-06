from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import bathroom
from django.core.mail import send_mail


# Create your views here.
def Home(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phonenumber = request.POST['number']
        user = User()
        user.username = username
        user.email = email
        user.phonenumber = phonenumber
        user.save()
        return HttpResponse("you are registration is successful")
    return render(request, "landingPage.html")


def uploadedImgs(request):
    image = bathroom.objects.all
    if image is not None:
        return render(request, 'selection.html', {'image': image})
    else:
        return HttpResponse("img not found")


def Mail_Service(request):
    subject = 'Testing Mail Service in Django'
    message = """"Dear Client Prashanth Chowdary"""
    from_email = 'your_email@gmail.com'
    recipient_list = ['mr.prashanthchowdary007@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return render(request, "mailsend.html")
