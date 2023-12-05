
from django import forms


class LoanForm(forms.ModelForm):
    class Meta:
        model = 