from django import template
from .slovo import CENSOR

register = template.Library()


@register.filter()
def censor(value):
    result = ''
    for x in value.split(' '):
        for y in CENSOR.split('/n'):
            if x == y:
                result += f'{x[0]}***{x[-1]} '
            else:
                result += f'{x} '
    return result

