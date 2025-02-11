from django.shortcuts import render, redirect

from products.models import Product
from review.forms import ReviewForm
from review.models import Review


# Create your views here.
def add_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = Product.objects.get(id=product_id)
            review.save()
            return redirect('products:detail', product_id=product_id)
    else:
        form = ReviewForm()
    return redirect('products:detail', product_id=product_id)