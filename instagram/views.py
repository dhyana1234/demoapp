from django.shortcuts import redirect, render

from demo.settings import EMAIL_HOST_USER
from .models import*
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def send_email_view(request):
    subject =  'Hello from django'
    message = 'This is a test email sent from django.'
    recipient = 'recipientemail@example.com'

    send_mail(subject, message, EMAIL_HOST_USER, [recipient])
    return HttpResponse('Email sent successfully!')

def hello(request):
    return render(request,'student.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            pwd = check_password(password,user.password)
            if pwd:
                return redirect('/student/')
            else:
                return render(request,'logintask.html',{'errorMsg':'Invalid password'})
        else:
            return render(request,'logintask.html',{'errorMsg':'Invalid Login'})
    return render(request,'logintask.html')  


def instagram(request):
    if request.method =="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if first_name and last_name and username and password:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            )
            user.set_password(password)
            user.save()

            return redirect('/instagram/')
        else:
            context = {"error": "All fields are required."}
            return render(request,'instagram.html', context)
    return render(request, 'instagram.html')




    


        


