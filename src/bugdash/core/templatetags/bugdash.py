from django.template import Library

register = Library()



@register.filter
def title(period):
    if not period.start
