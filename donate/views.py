from django.shortcuts import render
from .models import Payment

def Donate(request):
    # Get the first donate object
    donate = Payment.objects.first()
    context = {'donate': donate}
    return render(request, 'donate/donate.html', context)