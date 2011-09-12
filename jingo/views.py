import jingo


def direct_to_template(request, template, context=None, **kwargs):
    return jingo.render(request, template, context, **kwargs)
