from django.shortcuts import render
from bag.models import BagItem


# Create your views here.
def bag(request):
    return render(request, 'bag/bag.html', {"bag_items": BagItem.objects.filter(bag__user=request.user)})