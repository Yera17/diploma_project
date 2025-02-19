from django.db import transaction
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

        if make_stock_dealing(request, purchase_items):
            return redirect('bag:bag')

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

        cancel_stock_dealing(items)

        return redirect("bag:bag")

    return render(request, "bag/bag.html")

def buy(request, purchase_id):
    get_purchase = Purchase.objects.get(id=purchase_id)
    items = get_purchase.purchaseitem_set.all()

    if request.method == "POST":
        get_purchase.status = "Completed"
        get_purchase.save()
        buy_stock_dealing(items)

        bag = Bag.objects.get(user=request.user)
        bag.bagitem_set.all().delete()
        return redirect("/")

    return render(request, "purchase/purchase.html")

def make_stock_dealing(req, items):
    id_and_quantity = {}

    # Collect quantities in one pass
    for item in items:
        product_size_id = item.product_size.id
        id_and_quantity[product_size_id] = id_and_quantity.get(product_size_id, 0) + item.quantity

    try:
        with transaction.atomic():  # Ensures atomicity (prevents partial updates)
            for product_size_id, total_quantity in id_and_quantity.items():
                product_size = ProductSize.objects.select_for_update().get(id=product_size_id)

                # Prevent stock from going negative
                if product_size.number_in_stock < total_quantity:
                    messages.error(req, "Not enough stock available.")
                    return True  # Redirect if stock is insufficient

                product_size.number_in_stock -= total_quantity
                if product_size.number_in_stock == 0:
                    product_size.in_stock = False
                product_size.save()

    except Exception as e:  # Catch unexpected errors
        messages.error(req, e)
        return True

    return False

def cancel_stock_dealing(items):
    for item in items:
        product_size = ProductSize.objects.get(id=item.product_size.id)

        product_size.number_in_stock = product_size.number_in_stock + item.quantity

        product_size.save()
        size_dealing(product_size)

def buy_stock_dealing(items):
    for item in items:
        product_size = ProductSize.objects.get(id=item.product_size.id)
        size_dealing(product_size)

def size_dealing(product_size):
    total_in_stock = 0
    product = Product.objects.get(id=product_size.product_id)
    for size in product.sizes.all():
        total_in_stock += size.number_in_stock

    product.total_in_stock = total_in_stock
    product.save()

