from django.shortcuts import render
from textmagic.rest import TextmagicRestClient

def index(request):
    

    return render(request, "home/index.html")

