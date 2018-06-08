from django import template
register = template.Library()

@register.filter
def index(List, i):
    if List is None or len(List) <= i:
        return False
    else:
        return List[int(i)]