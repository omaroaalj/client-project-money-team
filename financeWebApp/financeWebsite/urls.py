from django.urls import path

from . import views

app_name = "financeWebsite"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("retirement/", views.retirement, name="retirement"),
    path("alternativeInvestments/", views.alternativeInvestments, name="alternativeInvestments"),
    path("lifeInsurance/", views.lifeInsurance, name="lifeInsurance"),
    path("healthcare/", views.healthcare, name="healthcare"),
]
