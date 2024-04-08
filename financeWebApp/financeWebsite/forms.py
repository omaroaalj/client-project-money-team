from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Enter your name:", max_length=100, required=True)
    email = forms.EmailField(label="Enter your email:", required=True)
    message = forms.CharField(label="Enter your message:", max_length=200, required=True)