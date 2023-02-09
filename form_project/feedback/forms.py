from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    feedback = forms.CharField()

