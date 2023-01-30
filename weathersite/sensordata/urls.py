from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sensor/<str:pk>/', views.SensorDetailView.as_view(), name='sensor'),
]
