# Allows custom HTML based on django implementations:
# https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
#
# Custom html views based on user groups:
# https://stackoverflow.com/questions/34571880/how-to-check-in-template-if-user-belongs-to-a-group
# Currently, groups aren't set up so implementing this would be more destructive than helpful.

# We also want to use this for the navbar 'active' item:
# https://stackoverflow.com/questions/340888/navigation-in-django

"""
Usage:
    1)  {% load core_tags %}
    2)  {% if request.user|has_group:"Student" %}
            <p>User belongs to Student
        {% else %}
            <p>User doesn't belong to Student</p>
        {% endif %}
"""

from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()