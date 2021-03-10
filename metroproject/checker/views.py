from django.shortcuts import render
from .models import Duty, Driver, Rota, MondayThursday, Friday, Saturday, Sunday, DoorCodes
import datetime as dt


# General logic
mapping = {'saturday': Saturday, 'sunday': Sunday, 'monday': MondayThursday, 'tuesday': MondayThursday,
           'wednesday': MondayThursday, 'thursday': MondayThursday, 'friday': Friday}
today = dt.date.today().isoformat()


# Views
def index(request):
    return render(request, 'checker/index.html')


def full_rota(request, given_date=today, daily=False):
    searched_date = request.GET.get('searched_date', given_date)
    given_date = searched_date
    parsed_date = dt.date.fromisoformat(given_date)
    rota_length = 126
    initial = dt.date(2020, 1, 11)
    tdelta = parsed_date - initial
    diff = tdelta.days % rota_length
    week = diff // 7
    day_no = diff % 7
    weekdays = list(mapping.keys())
    week_commencing = (parsed_date - dt.timedelta(days=day_no))
    next_week = parsed_date + dt.timedelta(days=7)
    prev_week = parsed_date - dt.timedelta(days=7)
    next_day = parsed_date + dt.timedelta(days=1)
    prev_day = parsed_date - dt.timedelta(days=1)
    table_dates = []
    for x in range(0, 7):
        table_day = week_commencing + dt.timedelta(days=x)
        table_dates.append(table_day.strftime('%a %Y-%m-%d'))
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
    context_weekly = {'mixed': mixed, 'drivers': drivers, 'weekdays': weekdays, 'chosen_day': weekdays[day_no],
                      'given_date': given_date, 'week_commencing': week_commencing, 'table_dates': table_dates,
                      'next_week': next_week, 'prev_week': prev_week, 'today': today, 'parsed_date': parsed_date}
    context_daily = {'mixed': mixed2, 'drivers': drivers, 'current_day': current_day, 'given_date': given_date,
                     'chosen_day': weekdays[day_no], 'details': details, 'next_day': next_day, 'prev_day': prev_day,
                     'today': today}
    if daily is False:
        return render(request, 'checker/full_rota.html', context_weekly)
    else:
        return render(request, 'checker/daily_checker.html', context_daily)


def all_duty_details(request, day=None):
    if day is not None:
        message = 'Selected duty range: '
        cls = mapping[day]
        if day in ('monday', 'tuesday', 'wednesday', 'thursday'):
            display_day = 'Monday - Thursday'
        else:
            display_day = day
        details = cls.objects.all().exclude(duty_id='OFF').exclude(duty_id='***').order_by('duty_id')
        context = {'details': details, 'day_range': day, 'display_day': display_day, 'message': message}
        return render(request, 'checker/all_duty_details.html', context)
    else:
        message = "Please choose a day below..."
        return render(request, 'checker/all_duty_details.html', context={'message': message})



def duty_details(request, day, duty):
    try:
        cls = mapping[day]
        details = cls.objects.get(duty=duty)
        context = {'day': day, 'duty': duty, 'details': details}
        return render(request, 'checker/duty_details.html', context)
    except:
        message = f'Duty number {duty} does not exist on {day.capitalize()}\'s schedule'
        return render(request, 'checker/error.html', context={'message': message})


def duty_card(request, day, duty):
    # parsing correct url due to unified duty card files name convention
    cls = mapping[day].__name__
    try:
        duty = Duty.objects.get(pk=duty)
        if duty.route == 'N134' and cls in ('Sunday', 'MondayThursday'):
            cls = 'Sunday_Thursday'
        elif duty.route == 'N134' and cls in ('Friday', 'Saturday'):
            cls = 'Friday_Saturday'
        file_name = '_'.join((duty.route, cls, duty.number)) + '.html'
        return render(request, f'checker/duty_cards/{duty.route}/{file_name}')
    except:
        message = 'No duty card here'
        return render(request, 'checker/error.html', context={'message': message})


def door_codes(request):
    codes = DoorCodes.objects.all()
    title = 'Door codes'
    return render(request, 'checker/door_codes.html', context={'codes': codes, 'title': title})


