from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib import messages
from bag.models import Bag
from products.models import ProductSize, Product
from purchase.models import Purchase, PurchaseItem


# Create your views here.
def make_purchase(request):
    if request.method == "POST":
        new_purchase = Purchase.objects.create(user=request.user)
        bag_id = request.POST.get('action')
        bag = Bag.objects.get(id=bag_id)
        total_price = 0
        bag_items = bag.bagitem_set.all()

        for bag_item in bag_items:
            PurchaseItem.objects.create(
                purchase=new_purchase,
                product_size=bag_item.productSize,
                quantity=bag_item.quantity,
                price=bag_item.productSize.product.price * bag_item.quantity,
            )

        purchase_items = new_purchase.purchaseitem_set.all()

        for purchase_item in purchase_items:
            total_price += purchase_item.price

        new_purchase.total_price = total_price
        try:
            stock_dealing(purchase_items, True)
        except IntegrityError:
            stock_dealing(purchase_items, False)
            new_purchase.delete()
            messages.error(request, "Not available quantity")
            return redirect("bag:bag")

        new_purchase.save()
        return redirect("purchase:purchase", new_purchase.id)
    return render(request, 'bag/bag.html')

def purchase(request, purchase_id):
    get_purchase = Purchase.objects.get(id=purchase_id)

    return render(request, "purchase/purchase.html", {
        "purchase": get_purchase,
        "items": get_purchase.purchaseitem_set.all(),
    })

def cancel_purchase(request, purchase_id):
    get_purchase = Purchase.objects.get(id=purchase_id)
    items = get_purchase.purchaseitem_set.all()
    if request.method == "POST":
        get_purchase.status = "Cancelled"
        get_purchase.save()

        stock_dealing(items, False)

        return redirect("bag:bag")

    return render(request, "bag/bag.html")

def buy(request, purchase_id):
    get_purchase = Purchase.objects.get(id=purchase_id)

    if request.method == "POST":
        get_purchase.status = "Completed"
        get_purchase.save()

        return redirect("/")

    return render(request, "purchase/purchase.html")

def stock_dealing(items, boolean):
    for item in items:
        total_in_stock = 0
        product_size = ProductSize.objects.get(id=item.product_size.id)
        product = Product.objects.get(id=product_size.product_id)
        if boolean:
            product_size.number_in_stock = product_size.number_in_stock - item.quantity
        else:
            product_size.number_in_stock = product_size.number_in_stock + item.quantity
        product_size.save()

        for size in product.sizes.all():
            total_in_stock += size.number_in_stock

        product.total_in_stock = total_in_stock
        product.save()