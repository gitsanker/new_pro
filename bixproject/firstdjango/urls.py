from django.urls import path
from .views import *
urlpatterns = [
    path('demo/', display),
    path('sample/', myformview),
    path('form/',formclassview),
    path('tables/', tablesview),
    path('search/', search),
    path('update/', update, name='updatequery'),
    path('delete/', deleterecord, name='deleterequest'),

]