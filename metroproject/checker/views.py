from django.shortcuts import render, HttpResponse
from .models import Duty, Driver, Rota
import datetime as dt

# Create your views here.
def index(request, given_date=dt.date.today()):
    rota_length = 126
    initial = dt.date(2020, 1, 11)
    tdelta = given_date - initial
    diff = tdelta.days % rota_length
    week = diff//7
    day_no = diff % 7
    weekdays = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    drivers = Driver.objects.all()
    rota = Rota.objects.values_list(*weekdays)
    current_rota = rota[week: len(rota)] + rota[:week]
    mixed = zip(drivers, current_rota)
    return render(request, 'checker/index.html', context={'mixed': mixed, 'rota': rota,
        'weekdays': weekdays, 'today': weekdays[day_no]})
