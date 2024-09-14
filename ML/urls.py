from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ML/', views.ML, name='ML'),
    path('Khodro45/', views.Khodro45, name='Khodro45'),
    path('Yazd2020/', views.Yazd2020, name='Yazd2020'),
    path('HamrahMechanic/', views.HamrahMechanic, name='HamrahMechanic'),
]
