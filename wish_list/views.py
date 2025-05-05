from django.contrib import messages
from django.shortcuts import render, redirect

import products.views
from wish_list.models import WishList, WishListItem


# Create your views here.
def wish_list(request):
    wishes = WishListItem.objects.all()
    return render(request, 'wish_list/wish_list.html', {"wishes": wishes})

def add_to_wish_list(request, product_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            wish, created = WishListItem.objects.get_or_create(wish_list=WishList.objects.get(user=request.user), product_id=product_id)
            if not created:
                messages.error(request, "This product is already in your wish list.")
        else:
            return redirect('my_app:login')
    return redirect('products:detail', product_id=product_id)

def remove_from_wish_list(request, wish_list_item_id):
    if request.method == "POST":
        WishListItem.objects.get(id=wish_list_item_id).delete()
        return redirect('wish_list:wish_list')
    return redirect('wish_list:wish_list')