from django.urls import path
from . models import Report
from . import views
from .views import ReportCreateView, ReportListView, ReportUpdateView, ReportDeleteView, ReportDetailView


urlpatterns = [
    #path("", views.index, name="index"),
    path('', ReportCreateView.as_view(), name="index"),
    path('reports', ReportListView.as_view(), name="reports"),
    path('report/<int:pk>/', ReportDetailView.as_view(), name="report-detail"),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name="report-update"),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name="report-delete"),
    path('report/<int:pk>/download', views.download, name='report-download'),
    #path("preview", views.preview, name="preview")
]