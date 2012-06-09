
# This app doesn't contain any models, but as its template tags need to
# be added to built-ins at start-up time, this is a good palce to do it.

from django.template.loader import add_to_builtins

add_to_builtins("overextends.templatetags.overextends_tags")
