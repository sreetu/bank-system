from django.shortcuts import render
from dbms.models import *


# Create your views here.
def index(request):
    return render(request,"dbms/homepage.html")

def about(request):
    return render(request,"dbms/AboutUs.html")

def contact(request):
    return render(request,"dbms/ContactUs.html")

def customer(request):
    details=CustomerDetails.objects.all()
    return render(request,"dbms/customer.html",{'detail':details})

def userpg(request,id):
    details=CustomerDetails.objects.get(id=id)
    return render(request, 'dbms/user.html', {'details':details})

def transfer(request,id):
    details = CustomerDetails.objects.get(id=id)
    return render(request, 'dbms/transfer.html', {'details': details})

def success(request):
    return render(request,"dbms/success.html")