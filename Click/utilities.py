import click
import time

@click.group()
def example():
    """ An example command with subcommands. """

@example.command()
def colors():
    click.echo('Non-styled output.')
    click.echo(click.style('Some styled output.', fg='blue'))
    click.secho('Styled using secho utility.', fg='black', bg='green')
    click.secho('Boldly styled using secho.', fg='black', bg='red', bold=True)


@example.command()
def clear():
    click.clear()

@example.command(name='progress-bar')
def progress_bar():
    click.echo('Processing values...')
    values = range(0, 100)
    with click.progressbar(values, label='Values') as bar:
        for value in bar:
            time.sleep(0.05)
    click.echo('Done.')

if __name__ == '__main__':
    example()
