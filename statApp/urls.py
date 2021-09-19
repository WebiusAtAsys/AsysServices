from django.urls import path
from . import views
from .views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name="stat-dashboard"),
    #path("preview", views.preview, name="preview")
]