from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/visualisations/', permanent=False)),
    path('', include('dashboard.urls')),
]
