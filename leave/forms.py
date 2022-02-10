from django import forms

from .models import Leave


class LeaveForm(forms.ModelForm):
    start_date = forms.DateField(
        label="What is your start date?", widget=forms.SelectDateWidget
    )
    end_date = forms.DateField(
        label="What is your end date?", widget=forms.SelectDateWidget
    )

    class Meta:
        model = Leave
        fields = "__all__"
