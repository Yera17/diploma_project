from django.shortcuts import render, get_object_or_404, redirect

from bag.forms import BagItemForm
from bag.models import Bag
from products.models import Product, Category
from review.forms import ReviewForm
from review.models import Review


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = product.sizes.all()
    values = ' | '.join([size.value for size in sizes])
    review_form = ReviewForm
    reviews = Review.objects.filter(product_id=product_id)


    if request.method == 'POST':
        form = BagItemForm(request.POST, product_id=product_id)
        if form.is_valid():
            bag_item = form.save(commit=False)
            bag_item.bag = Bag.objects.get(user=request.user)
            bag_item.save()
            return redirect('bag:bag')
    else:
        form = BagItemForm(product_id=product_id)



    return render(request, 'products/detail.html', {
        'product': product,
        'sizes': values,
        'form': form,
        'review_form': review_form,
        'reviews': reviews[::-1],
    })

def category_products(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = category.products.all()
    return render(request, 'products/category.html', {
        'products': products,
        'category': category,
    })