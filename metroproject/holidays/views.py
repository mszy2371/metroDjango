from django.shortcuts import render
from .models import Driver, EarlyWinter, Summer, LateWinter

# Create your views here.
def holidays(request):
    return render(request, 'holidays/holidays.html')