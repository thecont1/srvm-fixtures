from django.http import HttpResponse
from django.urls import path

NOTES = [
    "srvm detected this fixture from manage.py alone.",
    "DEBUG=True and an empty ALLOWED_HOSTS are fine on loopback.",
    "The virtualenv is bootstrapped from requirements.txt on first run.",
]


def index(_request):
    items = "".join(f"<li>{note}</li>" for note in NOTES)
    return HttpResponse(f"<h1>05 - django</h1><ul>{items}</ul>")


urlpatterns = [path("", index)]
