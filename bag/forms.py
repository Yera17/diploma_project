from django import forms

from products.models import ProductSize, Product
from .models import BagItem

class BagItemForm(forms.ModelForm):
    class Meta:
        model = BagItem
        fields = ['productSize', 'quantity']

    productSize = forms.ModelChoiceField(widget=forms.Select(attrs={
        'placeholder': 'Select Product Size',
        'title': 'Select Product Size',
        'class': 'w-full py-2 px-2 rounded-xl'
    }), initial='', queryset=ProductSize.objects.none())
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Select Quantity',
        'title': 'Select Quantity',
        'class': 'px-2 rounded-xl quantity-field',
        'min': '1',
        'max': '100',
    }), initial=1, required=False)

    def __init__(self, *args, product_id=None, **kwargs):
        super(BagItemForm, self).__init__(*args, **kwargs)

        if product_id:
            self.fields['productSize'].queryset = ProductSize.objects.filter(product_id=product_id, in_stock=True)
        else:
            # Use instance data if available
            if self.instance and self.instance.productSize_id:
                self.fields['productSize'].queryset = ProductSize.objects.filter(product_id=ProductSize.objects.get(id=self.instance.productSize_id).product_id, in_stock=True)
                if self.instance and self.instance.productSize.in_stock:
                    self.fields['quantity'].widget.attrs['max'] = self.instance.productSize.number_in_stock
            else:
                self.fields['productSize'].queryset = ProductSize.objects.none()  # Fallback to an empty queryset

