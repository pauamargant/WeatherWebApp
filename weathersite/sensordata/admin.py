from django.contrib import admin
from .models import Measure, Sensor, Measurement


# Admin classes for better user experience in the admin panel
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('value', 'unit', 'time', 'sensor')
    list_filter = ('sensor', 'unit', 'time')


class MeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')


class SensorAdmin(admin.ModelAdmin):
    list_display = ('room', 'description')
    list_filter = ('room', 'measurements')


admin.site.register(Measure, MeasureAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Sensor, SensorAdmin)
