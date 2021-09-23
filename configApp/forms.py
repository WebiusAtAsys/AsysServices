from django import forms
from .models import Filltexts


class FilltextsForm(forms.ModelForm):
    class Meta:
        model = Filltexts
        fields = '__all__'
        #exclude = ('author', 'pdf',)