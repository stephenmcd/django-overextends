
# This app doesn't contain any models, but as its template tags need to
# be added to built-ins at start-up time, this is a good place to do it.
import django

if django.VERSION < (1, 9):
    from django.template.base import add_to_builtins
    add_to_builtins("overextends.templatetags.overextends_tags")
