from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(
        label='firstname',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )
    lastname = forms.CharField(
        label='lastname',
        max_length=255,
        required=True,
        widget=forms.TextInput()
    )
