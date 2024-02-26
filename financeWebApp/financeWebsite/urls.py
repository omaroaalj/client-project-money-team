from django.urls import path

from . import views

app_name = "financeWebsite"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
]
