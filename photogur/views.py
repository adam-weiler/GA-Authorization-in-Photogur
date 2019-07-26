from django.http import HttpResponse #Needed to return an HttpResponse.
from django.shortcuts import render #Needed to render the page.
from photogur.models import Picture, Comment #Importing the classes from models.py file.

def pictures_page(request): # Redirects to http://localhost:8000/home/
    context = { 'pictures': Picture.objects.all() }

    # context = { 'pictures': 7 }

    response = render(request, 'pictures.html', context)
    return HttpResponse(response)