from django.shortcuts import render
from datetime import datetime
import json
# Create your views here.


def homepage(request):
    with open('data.json') as f:
        data = json.load(f)
        hello = 1
    return render(request, 'homepage.html', context={'people': data})

def about(request):
    numbers = range(0,1000)
    return render(request, 'about.html')

def today(request):

    return HttpResponse(str(datetime.today()))
