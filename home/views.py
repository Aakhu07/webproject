from django.shortcuts import render
from .models import *

def home(request):
    views = {}
    views['reviews'] = Review.objects.all()
    return render(request,'index.html',views)

def about(request):
    views = {}
    views['reviews'] = Review.objects.all()
    return render(request,'about.html',views)

def contact(request):
    views = {}
    views['informations'] = Information.objects.all()
    if request.method == "POST":
        my_name = request.POST['name']
        my_email = request.POST['email']
        my_subject = request.POST['subject']
        my_message = request.POST['message']
        data = Contact.objects.create(
            name = my_name,
            email = my_email,
            subject = my_subject,
            message = my_message
        )
        data.save()
        views['message']  = "Thank you. your message will be considered"
        return render(request, 'contact.html', views)

    return render(request,'contact.html',views)
def portfolio(request):
    return render(request,'portfolio.html')
def price(request):
    return render(request,'price.html')
def services(request):
    return render(request,'services.html')
