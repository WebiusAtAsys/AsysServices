from django.shortcuts import render
from mainApp.models import Report
from django.views.generic import TemplateView
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'statApp/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        labels = []
        data = []
        queryset = Report.objects.order_by('-date')
        for report in queryset:
            label = str(report.title) + " by " + str(report.author)
            labels.append(label)
            data.append(len(report.description))
        context = { 'labels': labels, 'data': data }
        return context


# def dashboard(request):
#     labels = []
#     data = []

#     queryset = Report.objects.order_by('-date')
#     for report in queryset:
#         labels.append(report.title)
#         data.append(report.date)
#     context = { 'labels': labels, 'data': data }
#     return render(request, "statApp/dashboard.html", context)