from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def get_user_display(context, user):
    """
    Customize the text if the value of the variable user is the request user.
    :param context: given by the template calling the method
    :param user: given by the template calling the method
    :return: a customized text if request user, otherwise the username.
    """

    if user == context['user']:
        return "Vous avez"

    return f"{user.username} a"
