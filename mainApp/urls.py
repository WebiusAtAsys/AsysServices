from django.urls import path
from . import views
from .views import ReportCreateView

urlpatterns = [
    #path("", views.index, name="index"),
    path('', ReportCreateView.as_view(), name="index"),
    path("preview", views.preview, name="preview")
]