from django.shortcuts import render, redirect

from bag.models import Bag
from purchase.models import Purchase, PurchaseItem


# Create your views here.
def make_purchase(request):
    if request.method == "POST":
        new_purchase = Purchase.objects.create(user=request.user)
        bag_id = request.POST.get('action')
        bag = Bag.objects.get(id=bag_id)
        total_price = 0

        for bag_item in bag.bagitem_set.all():
            PurchaseItem.objects.create(
                purchase=new_purchase,
                product_size=bag_item.productSize,
                quantity=bag_item.quantity,
                price= bag_item.productSize.product.price * bag_item.quantity,)

        for purchase_item in new_purchase.purchaseitem_set.all():
            total_price += purchase_item.price

        new_purchase.total_price = total_price
        new_purchase.save()
        return redirect("purchase:purchase", new_purchase.id)
    return render(request, 'bag/bag.html')

def purchase(request, purchase_id):
    get_purchase = Purchase.objects.get(id=purchase_id)
    return render(request, "purchase/purchase.html", {
        "purchase": get_purchase,
        "items": get_purchase.purchaseitem_set.all(),
    })