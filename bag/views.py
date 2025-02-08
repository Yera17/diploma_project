from django.shortcuts import render, redirect

from bag.forms import BagItemForm
from bag.models import BagItem
from django.forms import modelformset_factory

# Create your views here.
def bag(request):
    bag_items = BagItem.objects.filter(bag__user=request.user)

    BagItemFormSet = modelformset_factory(BagItem, form=BagItemForm, extra=0)

    if request.method == 'POST':
        formset = BagItemFormSet(request.POST, queryset=bag_items)
        if formset.is_valid():
            
            formset.save()
            return redirect('bag:bag')  # Redirect back to bag after updating
    else:
        formset = BagItemFormSet(queryset=bag_items)

    return render(request, 'bag/bag.html', {"bag_items": bag_items, "formset": formset})



