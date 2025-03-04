from django import forms

from products.models import ProductSize, Product
from .models import BagItem

class BagItemForm(forms.ModelForm):
    class Meta:
        model = BagItem
        fields = ['productSize', 'quantity']

    def clean_productSize(self):
        productSize = self.cleaned_data.get('productSize')
        if not productSize:
            raise forms.ValidationError("Product size is required.")
        return productSize

    productSize = forms.ModelChoiceField(widget=forms.Select(attrs={
        'placeholder': 'Select Product Size',
        'title': 'Select Product Size',
        'class': 'w-full py-2 px-2 rounded-xl'
    }), initial='', queryset=ProductSize.objects.none())
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Select Quantity',
        'title': 'Select Quantity',
        'class': 'px-2 rounded-xl',
        'min': '1',
        'max': '100',
    }), initial=1, required=False)

    def __init__(self, *args, product_id=None, **kwargs):
        super(BagItemForm, self).__init__(*args, **kwargs)

        if product_id:
            self.fields['productSize'].queryset = ProductSize.objects.filter(product_id=product_id)
        else:
            # Use instance data if available
            if self.instance and self.instance.productSize_id:
                self.fields['productSize'].queryset = ProductSize.objects.filter(product_id=ProductSize.objects.get(id=self.instance.productSize_id).product_id)
            else:
                self.fields['productSize'].queryset = ProductSize.objects.none()  # Fallback to an empty queryset

