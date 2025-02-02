from django.shortcuts import render
from products.models import Product, Category
# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'my_app/index.html', {
        'categories': categories,
        'products': products,
    })

def contact(request):
    return render(request, 'my_app/contact.html')
