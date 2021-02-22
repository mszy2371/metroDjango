from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Duty, Driver, Rota, MondayThursday, Friday, Saturday, Sunday
import datetime as dt


# General logic
mapping = {'saturday': Saturday, 'sunday': Sunday, 'monday': MondayThursday, 'tuesday': MondayThursday,
           'wednesday': MondayThursday, 'thursday': MondayThursday, 'friday': Friday}


# Views
def index(request):
    return render(request, 'checker/index.html')


def full_rota(request, given_date=(dt.date.today()).isoformat(), daily=False):
    if request.method == "POST":
        given_date = request.POST["searched_date"]
    parsed_date = dt.date.fromisoformat(given_date)
    rota_length = 126
    initial = dt.date(2020, 1, 11)
    tdelta = parsed_date - initial
    diff = tdelta.days % rota_length
    week = diff // 7
    day_no = diff % 7
    weekdays = list(mapping.keys())
    week_commencing = (parsed_date - dt.timedelta(days=day_no)).isoformat()
    drivers = Driver.objects.all()
    rota = Rota.objects.all().values_list(*weekdays)
    current_rota = rota[week: len(rota)] + rota[:week]
    mixed = zip(drivers, current_rota)
    cls = mapping[weekdays[day_no]]
    current_day = []
    details = []
    for line in current_rota:
        current_day.append(line[day_no])
        detail = cls.objects.get(duty_id=line[day_no])
        details.append(detail)
    mixed2 = zip(drivers, current_day, details)
    if daily is False:
        return render(request, 'checker/full_rota.html', context={'mixed': mixed, 'drivers': drivers,
        'weekdays': weekdays, 'chosen_day': weekdays[day_no], 'given_date': given_date,
        'week_commencing': week_commencing })
    else:
        return render(request, 'checker/daily_checker.html', context={'mixed': mixed2, 'drivers': drivers,
                                                                      'current_day': current_day, 'given_date': given_date,
                                                                      'chosen_day': weekdays[day_no], 'details': details})


# def new_details(request, given_date, daily=False):
#     if request.method == "POST":
#         given_date = request.POST["searched_date"]
#         if given_date is None or given_date is '':
#             given_date = (dt.date.today()).isoformat()
#         print(given_date)
#         return HttpResponseRedirect(reverse('full_rota', kwargs={'given_date': given_date}))


def all_duty_details(request):
    monday = MondayThursday.objects.all().exclude(duty_id='OFF').exclude(duty_id='***')
    friday = Friday.objects.all().exclude(duty_id='OFF').exclude(duty_id='***')
    saturday = Saturday.objects.all().exclude(duty_id='OFF').exclude(duty_id='***')
    sunday = Sunday.objects.all().exclude(duty_id='OFF').exclude(duty_id='***')
    return render(request, 'checker/all_duty_details.html',  context={'monday': monday, 'friday': friday,
                                                                      'saturday': saturday, 'sunday': sunday})


def duty_details(request,day, duty):
    cls = mapping[day]
    try:
        details = cls.objects.get(duty=duty)
        if details.duty_id == '***':
            details.start_time = 'duty time not specified'
            details.finish_time = ''
    except cls.DoesNotExist:
        raise Http404("This duty number does not exist on given day")
    return render(request, 'checker/duty_details.html', context={'day': day, 'duty': duty, 'details': details})




