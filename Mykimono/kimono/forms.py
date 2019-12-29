from django import forms


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
    email = forms.CharField(
        label='email',
        max_length=50,
        required=True,
        widget=forms.TextInput()
    )
    mobile_number = forms.CharField(
        label='Mobile number',
        max_length=50,
        required=True,
        widget=forms.TextInput()
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
