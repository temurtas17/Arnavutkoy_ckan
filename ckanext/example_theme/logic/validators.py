import ckan.plugins.toolkit as tk


def example_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "example_theme_required": example_theme_required,
    }
