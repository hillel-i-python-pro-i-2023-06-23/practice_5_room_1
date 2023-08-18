from django import forms


class EncryptForm(forms.Form):
    topic = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
