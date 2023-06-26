from django import template

register = template.Library()

@register.filter
def trans(value):
    return value
