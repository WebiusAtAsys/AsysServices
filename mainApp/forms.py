from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    #add some descriptive placeholders:
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Main title of the report'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your description here'}))

    class Meta:
        model = Report
        #fields = '__all__'
        exclude = ('author', 'pdf',)