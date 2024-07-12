from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def is_superuser(user):
    return user.is_superuser