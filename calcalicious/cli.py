import click


@click.command()
def cli():
    # click.echo('Hello, James')
    val = addition(2)
    click.echo(val)


def addition(x):
    if x == 0:
        return 0
    return x + x