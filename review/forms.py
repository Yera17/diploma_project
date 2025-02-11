from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'title', 'rating']

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    rating = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))