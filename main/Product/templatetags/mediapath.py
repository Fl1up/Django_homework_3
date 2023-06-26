from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def mediapath(imag):
    return settings.MEDIA_URL + imag