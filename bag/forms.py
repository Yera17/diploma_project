# from django import forms
#
# from .models import BagItem
#
# class BagItemForm(forms.ModelForm):
#     class Meta:
#         model = BagItem
#         fields = ['size', 'quantity']
#
#     size = forms.ChoiceField(choices=BagItem.productSize.product.sizes)
#     quantity = forms.ChoiceField(choices=[1,2,3,4,5,6,7,8,9,10])