from django.shortcuts import render
from .models import Driver, EarlyWinter, Summer, LateWinter



def holidays(request, year=None):
    if year is not None:
        drivers = Driver.objects.values_list('name', 'block_id', f'block__year_{year}', f'block__summer__year_{year}',
                                    f'block__common_block__year_{year}')
        message = f'Holidays in year {year}'
    else:
        drivers = Driver.objects.all()
        message = 'Choose a year below...'
    context = {'drivers': drivers, 'message': message, 'year': year}
    return render(request, 'holidays/holidays.html', context)
