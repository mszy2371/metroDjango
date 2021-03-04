from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('full_rota/', views.full_rota, {'daily': False}, name='full_rota_solo'),
    path('full_rota/<given_date>/', views.full_rota, {'daily': False}, name='full_rota'),
    path('full_rota/<searched_date>/', views.full_rota, {'daily': False}, name='full_rota2'),
    path('duty_details/', views.all_duty_details, name='all_duty_details'),
    path('duty_details/<day_range>/', views.all_duty_details, name='all_duty_details_spec'),
    path('duty_details/<day>/<duty>/', views.duty_details, name='duty_details'),
    path('daily_checker/', views.full_rota, {'daily': True}, name='daily_checker_today'),
    path('daily_checker/<given_date>/', views.full_rota, {'daily': True}, name='daily_checker'),
    path('duty_card/<day>/<duty>/', views.duty_card, name='duty_card'),
]