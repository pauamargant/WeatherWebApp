from django.urls import path
from . import views
urlpatterns = [
    path('insert/', views.insert_measurement, name='insert_measurement'),
]
