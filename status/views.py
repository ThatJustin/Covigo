from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@login_required
@never_cache
def index(request):
    return render(request, 'status/index.html')


@login_required
@never_cache
def patient_reports(request):
    return render(request, 'status/patient-reports.html', {
        'patient_reports': []
    })
