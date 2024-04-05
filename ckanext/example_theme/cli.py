import click


@click.group(short_help="example_theme CLI.")
def example_theme():
    """example_theme CLI.
    """
    pass


@example_theme.command()
@click.argument("name", default="example_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [example_theme]
