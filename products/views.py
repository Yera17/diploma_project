from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.
def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = product.sizes.all()
    values = ' | '.join([size.value for size in sizes])
    return render(request, 'products/detail.html', {'product': product, 'sizes': values})