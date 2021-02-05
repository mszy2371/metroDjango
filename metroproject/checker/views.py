from django.shortcuts import render, HttpResponse
from .models import Duty, Driver, Rota, MondayThursday, Friday, Saturday, Sunday
import datetime as dt

# Create your views here.


def index(request):
    return render(request, 'checker/index.html')

def full_rota(request, given_date=(dt.date.today()).isoformat()):
    parsed_date = dt.date.fromisoformat(given_date)
    rota_length = 126
    initial = dt.date(2020, 1, 11)
    tdelta = parsed_date - initial
    diff = tdelta.days % rota_length
    week = diff//7
    day_no = diff % 7
    weekdays = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    drivers = Driver.objects.all()
    rota = Rota.objects.values_list(*weekdays)
    current_rota = rota[week: len(rota)] + rota[:week]
    mixed = zip(drivers, current_rota)
    return render(request, 'checker/full.rota.html', context={'mixed': mixed, 'rota': rota,
        'weekdays': weekdays, 'chosen_day': weekdays[day_no], 'chosen_date': given_date,
        'week_commencing': 'tbc'})

def duty_details(request, day, duty):
    pass


