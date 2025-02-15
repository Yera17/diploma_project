from django import template

register = template.Library()

@register.filter
def times(number):
    return range(int(number))

@register.filter
def five_minus_times(number):
    if number-int(number) == 0.5:
        return range(4 - int(number))
    return range(5-int(number))

@register.filter
def is_point_five(number):
    if number-int(number) == 0.5:
        return True
    return False