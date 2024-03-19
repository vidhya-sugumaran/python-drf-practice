from django import forms

from .models import LMS

class BookForm(forms.ModelForm):
    class Meta:
        model = LMS
        fields = "__all__"