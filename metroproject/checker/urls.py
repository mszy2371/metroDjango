from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('full_rota/today/', views.full_rota, {'daily': False}, name='full_rota_today'),
    path('full_rota/<given_date>/', views.full_rota, {'daily': False}, name='full_rota'),
    path('duty_details/', views.all_duty_details, name='all_duty_details'),
    path('duty_details/<day>/<duty>/', views.duty_details, name='duty_details'),
    path('daily_checker/today/', views.full_rota, {'daily': True}, name='daily_checker_today'),
    path('daily_checker/<given_date>/', views.full_rota, {'daily': True}, name='daily_checker'),
]