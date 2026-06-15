from django.shortcuts import render


def visualisations(request):
    return render(request, 'dashboard/visualisations.html')


def ml_results(request):
    return render(request, 'dashboard/ml_results.html')
