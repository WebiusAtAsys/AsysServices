from django.shortcuts import render
from mainApp.models import Report
from django.views.generic import TemplateView
#from usersApp.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'statApp/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report_dict = {}
        labels = []
        data = []

        reports = Report.objects.all()
        for report in reports:
            print("i am here")
            print("author: ", str(report.author))
            if str(report.author) not in report_dict.keys():
                report_dict[str(report.author)] = 1
            else:
                report_dict[str(report.author)] += 1
            print("report dict", report_dict)
        labels = list(report_dict.keys())
        data = list(report_dict.values())
        print("lables:", labels)
        print("data: ", data)
        ################ for a different graph #####################
        # for report in queryset:
        #     label = str(report.title) + " by " + str(report.author)
        #     labels.append(label)
        #     data.append(len(report.description))

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