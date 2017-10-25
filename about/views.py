from django.shortcuts import render
from .models import AboutUs

def About(request):
    # Get the first about us object
    about_us = AboutUs.objects.first()
    context = {'about_us': about_us}
    return render(request, 'about/about.html', context)