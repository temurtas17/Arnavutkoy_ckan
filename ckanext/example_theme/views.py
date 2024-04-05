from flask import Blueprint


example_theme = Blueprint(
    "example_theme", __name__)


def page():
    return "Hello, example_theme!"


example_theme.add_url_rule(
    "/example_theme/page", view_func=page)


def get_blueprints():
    return [example_theme]
