from django.db import models
from django.urls import reverse


class Measure(models.Model):
    """Used to specify which measurement can a sensor do (f. ex Temeprature)"""
    name = models.CharField(max_length=20, primary_key=True)
    unit = models.CharField(max_length=10)
    description = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.unit


class Sensor(models.Model):
    """Model used to store information about sensors"""
    # Fields
    id = models.CharField(max_length=20, primary_key=True)
    room = models.CharField(
        max_length=20, help_text='Enter the room in which the sensor sits')
    measurements = models.ManyToManyField(Measure)
    description = models.CharField(
        max_length=200, help_text="Enter, if necessary, additional information about the sensor")

    def __str__(self):
        """String representating the sensor"""
        return f"Sensor {self.room}"

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model"""
        return reverse("model-detail-view", args=[str(self.id)])


class Measurement(models.Model):
    """Class used to store each individual measurement made by a sensor"""
    value = models.FloatField()
    unit = models.ForeignKey('Measure', on_delete=models.CASCADE)
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        models.UniqueConstraint(
            fields=['time', 'sensor'], name="unique_measure_sensor")
        ordering = ['-time']

    def __str__(self):
        return f"{self.value}{self.unit.unit} ({self.time})"
