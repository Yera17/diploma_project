from django import forms
from products.models import ProductSize
from .models import BagItem, Bag


class BagItemForm(forms.ModelForm):
    class Meta:
        model = BagItem
        fields = ['productSize', 'quantity', 'bag']

    productSize = forms.ModelChoiceField(queryset=ProductSize.objects.all())
    quantity = forms.IntegerField(required=False)
    bag = forms.ModelChoiceField(queryset=Bag.objects.all())

