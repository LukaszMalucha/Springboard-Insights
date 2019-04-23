from django.shortcuts import render


def dashboard(request):

    return render(request, "dashboard.html")

def rest(request):
    return render(request, "rest.html")