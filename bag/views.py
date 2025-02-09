from django.shortcuts import render, redirect, get_object_or_404

from bag.forms import BagItemForm
from bag.models import BagItem, Bag
from django.forms import modelformset_factory

# Create your views here.
def bag(request):
    the_bag = Bag.objects.get(user=request.user)
    bag_items = BagItem.objects.filter(bag=the_bag)
    bag_item_form_set = modelformset_factory(BagItem, form=BagItemForm, extra=0)

    if request.method == 'POST':
        formset = bag_item_form_set(request.POST or None, queryset=bag_items)
        if formset.is_valid():
            for form in formset:
                print(form.instance.id)
                if form.has_changed():
                    bag_item = form.save(commit=False)
                    bag_item.bag = the_bag # Ensure the correct bag association
                    bag_item.save()
            return redirect('bag:bag')
        else:
            return redirect('bag:bag')

    else:
        formset = bag_item_form_set(queryset=bag_items)

    return render(request, 'bag/bag.html', {"bag_items": bag_items, "formset": formset})

def delete_bag_item(request, bag_item_id):
    bag_item = get_object_or_404(BagItem, id=bag_item_id)

    if request.method == 'POST':
        # Perform deletion on confirmation
        bag_item.delete()
        return redirect('bag:bag')

    return render(request, 'bag/delete_bag_item.html', {'bag_item': bag_item})



