Click
=====

Make composable Python command line applications.

Documentation
-------------

See official documentation: http://click.pocoo.org/latest/

Hello, World!
-------------

An example with a command and a couple options:

```
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```

Examples
--------

- Hello, World: [hello.py](hello.py)
- Options: [options.py](options.py)
  - Basic values
  - Choices
  - Boolean
  - Feature switches
  - [More on options](http://click.pocoo.org/latest/options/)
- Arguments: [arguments.py](arguments.py)
  - Variadic arguments
  - [More on arguments](http://click.pocoo.org/latest/arguments/)
- Commands: [commands.py](commands.py)
  - Sub-commands
  - [More on commands](http://click.pocoo.org/latest/commands/)
- Utilities: [utilities.py](utilities.py):
  - Colors
  - Progress bars
  - Screen clearing
  - [More on utilities](http://click.pocoo.org/6/utils/)

Tutorial
----------

https://github.com/tylerdave/Click-Tutorial
