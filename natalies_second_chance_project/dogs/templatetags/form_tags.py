from django import template

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def add_label_class(field, css_class):
    return field.label_tag(attrs={'class': css_class})

@register.filter
def form_group_style(bound_field):
    css_class=""
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'has-danger'
        else:
            # may need to be refactored if you want to not have green highlighting for specific field types
            # that is wy the field_type filter is up above ( to check for something like a password field type or something)
            css_class = 'has-success'
    else:
        css_class = 'has-primary'
    return f'floating-label form-group {css_class}'