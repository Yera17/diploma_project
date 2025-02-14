from django.shortcuts import render, redirect, get_object_or_404

from bag.forms import BagItemForm
from bag.models import BagItem, Bag
from django.forms import modelformset_factory
import re

# Create your views here.
def bag(request):
    the_bag = Bag.objects.get(user=request.user)
    bag_items = BagItem.objects.filter(bag=the_bag)
    bag_item_form_set = modelformset_factory(BagItem, form=BagItemForm, extra=0)

    if request.method == 'POST':
        action = request.POST.get('action')
        formset = bag_item_form_set(request.POST or None, queryset=bag_items)
        if action == 'update':
            if formset.is_valid():
                for form in formset:
                    if form.has_changed():
                        bag_item = form.save(commit=False)
                        bag_item.bag = the_bag # Ensure the correct bag association
                        bag_item.save()
                return redirect('bag:bag')
            else:
                return redirect('bag:bag')
        elif 'delete' in action:
            match = re.search(r'\d+', action)
            delete_bag_item(int(match.group()))
            return redirect('bag:bag')
        elif 'add' in action:
            match = re.search(r'\d+', action)
            create_bag_item(int(match.group()))
            return redirect('bag:bag')
    else:
        formset = bag_item_form_set(queryset=bag_items)

    return render(request, 'bag/bag.html', {"bag_items": bag_items, "formset": formset})

def create_bag_item(bag_item_id):
    bag_item = BagItem.objects.get(id=bag_item_id)
    BagItem.objects.create(bag=bag_item.bag, productSize=bag_item.productSize, quantity=bag_item.quantity)

def delete_bag_item(bag_item_id):
    bag_item = get_object_or_404(BagItem, id=bag_item_id)
    bag_item.delete()




