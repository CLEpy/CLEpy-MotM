import click

@click.group()
@click.option('--verbose', '-v', is_flag=True)
@click.pass_context
def example(ctx, verbose):
    """ An example command with subcommands. """
    ctx.obj = {}
    ctx.obj['verbose'] = verbose

@example.command()
@click.pass_context
@click.option('--name', default='World')
def hello(ctx, name):
    if ctx.obj['verbose']:
        click.echo('About to say hello...')
    click.echo('Hello, %s!' % name)

@example.command()
@click.pass_context
@click.option('--name', default='World')
def goodbye(ctx, name):
    if ctx.obj['verbose']:
        click.echo('About to say goodbye...')
    click.echo('Goodbye, %s!' % name)


if __name__ == '__main__':
    example()
