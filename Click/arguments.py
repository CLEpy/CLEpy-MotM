import click

@click.command()
@click.argument('names', nargs=-1)
def hello(names):
    """Simple program that greets all of the NAMES provided."""
    for name in names:
        click.echo('Hello, %s!' % name)

if __name__ == '__main__':
    hello()
