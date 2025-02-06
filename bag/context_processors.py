from .models import Bag


def my_bag(request):
    if request.user.is_authenticated:
        try:
            bag = Bag.objects.get(user=request.user)
            return {'my_bag': bag}
        except Bag.DoesNotExist:
            return {'my_bag': None}
    return {'my_bag': None}
