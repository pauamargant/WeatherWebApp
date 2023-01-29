from django.shortcuts import render
from .models import Measure, Sensor, Measurement


def index(request):
    """View function for home page of site"""
    # Generate count of some of the main objects:
    num_sensors: int = Sensor.objects.all().count()
    num_measurements: int = Measurement.objects.all().count()
    num_measure: int = Measure.objects.all().count()

    context = {'num_sensors': num_sensors,
               'num_measurements': num_measurements,
               'num_measures': num_measure,
               'sensors': Sensor.objects.all(),
               'measurements': Measurement.objects.all()
               }
    return render(request, 'index.html', context=context)
