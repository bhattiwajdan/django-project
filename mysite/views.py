from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")


def buttons(request):
    return render(request, "buttons.html")


def typography(request):
    return render(request, "typography.html")


def mdi(request):
    return render(request, "mdi.html")


def basic_elements(request):
    return render(request, "basic_elements.html")


def chartjs(request):
    return render(request, "chartjs.html")


def basic_table(request):
    return render(request, "basic-table.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def blankpage(request):
    return render(request, "blank-page.html")


def error404(request):
    return render(request, "error-404.html")


def error500(request):
    return render(request, "error-500.html")


def form(request):
    sum = 0
    try:
        if request.method == "POST":  # If the form has been submitted...
            num1 = request.POST["number 1"]
            num2 = request.POST["number 2"]
            sum = float(num1) + float(num2)
    except:
        pass
    return render(request, "form.html", {"output": sum})
