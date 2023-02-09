from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=7, min_length=2, error_messages={
        'max_length': 'You write more characters',
        'min_length': 'You write less characters',
        'required': 'You should write something',
    })
    rating = forms.IntegerField(max_value=5, min_value=1)
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2, 'cols': 20}))

