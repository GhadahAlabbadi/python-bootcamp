from django.shortcuts import render
from django.views.generic import TemplateView

class DashboardHomeView(TemplateView):
    template_name = 'dashboard/home.html'

def reports(request):
    return render(request, 'dashboard/reports.html')