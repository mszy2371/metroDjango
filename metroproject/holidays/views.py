from django.shortcuts import render
from .models import Driver, EarlyWinter, Summer, LateWinter
from django.db.models import F

# Create your views here.
def holidays(request):
    chosen_year = request.GET.get('year')
    if chosen_year is not None:
        year = 'Our holidays in' + chosen_year.split('_')[1]
        drivers = Driver.objects.values_list('name', 'block_id', f'block__{chosen_year}', f'block__summer__{chosen_year}',
                                    f'block__common_block__{chosen_year}')
    else:
        year = 'Please choose a year...'
        drivers = Driver.objects.all()
    return render(request, 'holidays/holidays.html', context={'drivers': drivers, 'year':year })
