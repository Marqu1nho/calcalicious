import click
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))
from calcalicious.sevice import addition


class Context:
    def __init__(self, numbers):
        self.numbers = numbers
        self.addition = addition.Addition()

@click.group()
@click.option("-n", "--numbers", help="Numbers to act on.")
@click.pass_context
def cli(ctx,numbers):
    """
    Takes passed in numbers and performs one of the following commands:
        -add (adds the numbers together) i.e. "[...]-n 1,2 add" [returns: 3]
    """
    ctx.obj = Context(numbers)


@cli.command() 
@click.pass_context
def add(ctx):
    result = ctx.obj.addition.add(numbers=ctx.obj.numbers)
    click.echo(result)
