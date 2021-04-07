from django.urls import path

from . import views

app_name = 'holidays'

urlpatterns = [
    path('', views.holidays, name='holidays'),
    path('year/<int:year>/', views.holidays, name='holidays_spec'),
]