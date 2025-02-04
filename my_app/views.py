from django.shortcuts import render, redirect
from products.models import Product, Category
from .forms import SignUpForm
from .models import UserProfile
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'my_app/index.html', {
        'categories': categories,
        'products': products,
    })

def contact(request):
    return render(request, 'my_app/contact.html')

def about(request):
    return render(request, 'my_app/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            user.save()
            UserProfile.objects.create(user=user, photo=form.cleaned_data['photo'])
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'my_app/signup.html', {
        'form': form,
    })
