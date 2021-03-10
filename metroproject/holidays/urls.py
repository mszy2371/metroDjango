from django.urls import path

from . import views

urlpatterns = [
    path('', views.holidays, name='holidays'),
    path('<year>/', views.holidays, name='holidays_spec'),
    path('test/', views.test, name='test'),
]