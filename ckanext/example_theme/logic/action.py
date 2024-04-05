import ckan.plugins.toolkit as tk
import ckanext.example_theme.logic.schema as schema


@tk.side_effect_free
def example_theme_get_sum(context, data_dict):
    tk.check_access(
        "example_theme_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.example_theme_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'example_theme_get_sum': example_theme_get_sum,
    }
