from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('full_rota/today/', views.full_rota, name='full_rota_today'),
    path('full_rota/<given_date>/', views.full_rota, name='full_rota')
]