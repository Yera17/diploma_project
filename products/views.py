from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from bag.forms import BagItemForm

# Create your views here.
def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = product.sizes.all()
    values = ' | '.join([size.value for size in sizes])

    if request.method == 'POST':
        form = BagItemForm(request.POST)
        if form.is_valid():
            bag_item = form.save()
            bag_item.save()
            return redirect('bag:bag')
    else:
        form = BagItemForm()

    return render(request, 'products/detail.html', {'product': product, 'sizes': values, 'form': form})