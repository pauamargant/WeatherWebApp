from django.shortcuts import render
from django.views import generic
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


class SensorDetailView(generic.DetailView):
    model = Sensor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["measures_names"] = ', '.join(
            [m.name for m in context["sensor"].measurements.all()])

        

        return context
