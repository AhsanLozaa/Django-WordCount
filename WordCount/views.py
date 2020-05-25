from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello")


def eggs(request):
    return HttpResponse("<h1>Hello, eggs are great</h1>")

