from django import forms


class DateForm(forms.Form):

    date_form = forms.DateInput(format=('%d-%m-%Y'))

    class Meta:
        fields = ['date']