from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Your name:", max_length=100, required=True)
    email = forms.EmailField(label="Your email:", required=True)
    message = forms.CharField(label="Your message:", widget=forms.Textarea, max_length=200, required=True)
