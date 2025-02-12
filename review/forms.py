from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'title', 'rating']

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'p-3 rounded-xl w-full min-w-0',
        'placeholder': 'Title...',
    }))

    RATING_CHOICES = [(x / 2, str(x / 2)) for x in range(2, 11)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={
            'class': 'p-3 rounded-xl w-full min-w-0',
        })
    )

    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'p-3 rounded-xl w-full min-w-0',
        'rows': 3,
        'placeholder': 'Write your review...',
    }))