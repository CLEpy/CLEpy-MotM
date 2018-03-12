import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', default='World', help='The person to greet.')
@click.option('--color', type=click.Choice(['red', 'green', 'blue']))
@click.option('--excited/--not-excited', default=True)
@click.option('--bold', is_flag=True)
def hello(count, name, color, excited, bold):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        punctuation = '!' if excited else '.'
        click.secho('Hello, %s%s' % (name, punctuation), fg=color, bold=bold, )

if __name__ == '__main__':
    hello()
