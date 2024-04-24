from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import ContactEntry
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, "financeWebsite/landingPage.html")

def contact(request):
    form = ContactForm()
    return render(request, "financeWebsite/contact.html", {"form": form})

def about(request):
    return render(request, "financeWebsite/about.html")

def services(request):
    return render(request, "financeWebsite/services.html")

def retirement(request):
    return render(request,"financeWebsite/retirement.html")

def alternativeInvestments(request):
    return render(request,"financeWebsite/alternativeInvestments.html")

def lifeInsurance(request):
    return render(request,"financeWebsite/lifeInsurance.html")

def healthcare(request):
    return render(request,"financeWebsite/healthcare.html")


def submit_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_message = form.cleaned_data["message"]
            contact_entry = ContactEntry(name=new_name, email=new_email, message=new_message)
            contact_entry.save()
            return HttpResponseRedirect("/thanks/")
    else:
        form = ContactForm()
    return render(request, "financeWebsite/contact.html", {"form": form})


def thanks(request):
    return render(request, "financeWebsite/thanks.html")