from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.template import Library

user_model = get_user_model()
register = Library()

@register.filter
def author_details(author, current_user=None):
    # Handle wrong author or current_user datatype
    if not isinstance(author, user_model):
        return ""
    # Display the blog's author name on the blog 
    if author == current_user:
        name = format_html("<strong>me</strong>")
    elif author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"
    # Display a link to the email address of the blog's author
    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html('</a>')
    else:
        prefix = ''
        suffix = ''

    return format_html("{}{}{}", prefix, name, suffix)
