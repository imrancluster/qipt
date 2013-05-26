from django import forms

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class AsteriskForm(forms.Form):

    name = forms.CharField(max_length=100)
    bind = forms.CharField(max_length=50)
    secret = forms.CharField(max_length=50, min_length=3)
    user = forms.CharField(max_length=50, min_length=3)

    email = forms.EmailField(required=False)
    mobile = forms.CharField(max_length=15, required=False)


