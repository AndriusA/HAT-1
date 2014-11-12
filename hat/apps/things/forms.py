from django import forms
from suit.widgets import SuitSplitDateTimeWidget
from .models import Thing

import datetime

class CSVExportForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    start_date = forms.DateTimeField(
        widget=SuitSplitDateTimeWidget,
        initial=datetime.datetime.now
    )

    end_date = forms.DateTimeField(
        widget=SuitSplitDateTimeWidget,
        initial=datetime.datetime.now
    )

    device = forms.ModelChoiceField(
        queryset=Thing.objects.all(),
        required=False
    )