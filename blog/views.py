from urllib.request import Request
from django.shortcuts import render
import requests
import json


# Create your views here.

def blog(request):

    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url)
    mensaje = ''
    if response.status_code == 200:
        response_json = json.loads(response.text)
        #results = response_json['results']
        

    return render(request, 'blogs/blog.html', {'response':response, 'response_json':response_json,})