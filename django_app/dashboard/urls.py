from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('visualisations/', views.visualisations, name='visualisations'),
    path('machine-learning/', views.ml_results, name='ml_results'),
]
