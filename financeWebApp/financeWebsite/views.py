from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "financeWebsite/landingPage.html")

def contact(request):
    return render(request, "financeWebsite/contact.html")
