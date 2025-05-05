from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bag.models import Bag
from products.models import Product, Category
from purchase.models import Purchase
from wish_list.models import WishList
from .forms import SignUpForm
from .models import UserProfile
def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(in_stock=True)
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
            Bag.objects.create(user=user)
            WishList.objects.create(user=user)
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'my_app/signup.html', {
        'form': form,
    })

def profile(request, user_id):
    if request.user.id != user_id:
        return redirect('my_app:login')
    
    user = User.objects.get(id=user_id)
    purchases = Purchase.objects.filter(user=user).order_by('-created_at')

    return render(request, 'my_app/profile.html', {"user":user, "purchases":purchases})
