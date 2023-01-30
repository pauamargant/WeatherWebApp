from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sensor/<int:pk>/', views.SensorDetailView.as_view(), name='sensor'),
]
