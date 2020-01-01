from django import forms
from .models import GENDER_CHOICES

class MessageForm(forms.Form):
    message = forms.CharField(
        label='firstname',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
    lastname = forms.CharField(
        label='lastname',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='email',
        max_length=50,
        required=True,
        widget=forms.EmailInput()
    )
    gender = forms.ChoiceField(
    label="性別",
    choices=GENDER_CHOICES,
    required=False
    )
    mobile_number = forms.IntegerField(
        label='Mobile number',
        required=True,
        widget=forms.NumberInput()
    )
    hotel = forms.fields.ChoiceField(
    label="Hotel",
    required=True,
    widget=forms.widgets.Select(),
    )
    hotel_another = forms.CharField(
        label='If you choose another',
        max_length=50,
        required=False,
        widget=forms.TextInput()
    )
    date = forms.DateField(
        label='Date',
        required=True,
        widget=forms.DateInput()
    )
    time = forms.TimeField(
        label='Time',
        required=True,
        widget=forms.TimeInput()
    )
    kimono_select = forms.fields.ChoiceField(
    label="kimono",
    required=True,
    widget=forms.widgets.Select(),
    )
    pay_type = forms.fields.ChoiceField(
    label="Pay_type",
    required=True,
    widget=forms.widgets.Select(),
    )
    card_number = forms.IntegerField(
        label='Card number',
        required=True,
        widget=forms.NumberInput()
    )
    expiry_date = forms.fields.ChoiceField(
    label="Expiry Date",
    required=True,
    widget=forms.widgets.Select(),
    )
    expiry_year = forms.fields.ChoiceField(
    label="year",
    required=True,
    widget=forms.widgets.Select(),
    )
    security_code = forms.CharField(
        label='security_code',
        max_length=5,
        required=True,
        widget=forms.TextInput()
    )
    free_zone = forms.CharField(
        label='free_zone',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )
