from itertools import product

from django.shortcuts import render, get_object_or_404, redirect

from bag.forms import BagItemForm
from bag.models import Bag
from products.models import Product, Category
from review.forms import ReviewForm
from review.models import Review


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    sizes = product.sizes.filter(in_stock=True)
    values = ' | '.join([size.value for size in sizes])
    unavailable_sizes = product.sizes.filter(in_stock=False)
    unavailable_values = ' | '.join([size.value for size in unavailable_sizes])
    review_form = ReviewForm
    reviews = Review.objects.filter(product_id=product_id)
    average_review = 0

    if reviews:
        average_review = to_average(reviews)

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = BagItemForm(request.POST, product_id=product_id)
            action = request.POST.get('action')
            if form.is_valid():
                bag_item = form.save(commit=False)
                bag_item.bag = Bag.objects.get(user=request.user)
                bag_item.save()
                if action == 'buy':
                    return redirect('bag:bag')
        else:
            return redirect('my_app:login')
    else:
        form = BagItemForm(product_id=product_id)

    return render(request, 'products/detail.html', {
        'product': product,
        'unavailable_sizes': unavailable_values,
        'sizes': values,
        'form': form,
        'review_form': review_form,
        'reviews': reviews[::-1],
        'average_review': average_review,
        'count': len(reviews),
    })

def category_products(request, category_name):
    if category_name in Category.objects.all().values_list('name', flat=True):
        category = get_object_or_404(Category, name=category_name)
        products = category.products.filter(in_stock=True)
        types = products.values_list('type', flat=True).distinct()
    else:
        products = Product.objects.filter(type=category_name)
        category = products.first().category
        types = category.products.filter(in_stock=True).values_list('type', flat=True).distinct()
    return render(request, 'products/category.html', {
        'products': products,
        'category': category,
        'types': types,
    })

def to_average(reviews):
    sum_of_ratings = 0
    for review in reviews:
        sum_of_ratings = sum_of_ratings + review.rating
    return sum_of_ratings / len(reviews)