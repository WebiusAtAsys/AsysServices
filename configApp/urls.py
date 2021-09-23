from django.urls import path
from .views import FilltextsCreateView, FilltextsUpdateView

urlpatterns = [
    path('', FilltextsCreateView.as_view(), name="config-create"),
    path('update', FilltextsUpdateView.as_view(), name="config-update"),
    #path("preview", views.preview, name="preview")
]