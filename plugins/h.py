#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" heart_sutra """

import click
import os
import sys
import inspect
from plugins.mods.heart_sutra_text import heart_sutra
from plugins.mods.heart_sutra import get_hint, get_sutra_length, check_sutra_line, quiz


# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    heart_sutra
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def p():
    """heart sutra practice"""
    quiz(heart_sutra)

@cli.command()
def w():
    """heart sutra webpage"""
    url = 'https://shanenull.com/buddhism/2024/heart_sutra/'
    click.launch(url)

# @cli.command()
# def h():
#     """hint"""
#     # prompt for line number
#     line = 0
#     hint = get_hint(heart_sutra, line)
#     click.echo(hint)


@cli.command()
def s():
    """show the heart sutra"""
    for h in heart_sutra:
        click.echo(h)


@cli.command()
def l():
    """show heart sutra length"""
    length = get_sutra_length(heart_sutra)
    click.echo(f"{length} lines")


# @cli.command()
# def z():
#     """check line 0"""
#     text = click.prompt(text="type the next line of the sutra")
#     check = check_sutra_line(heart_sutra, 0, text)
#     if check:
#         click.echo(f"{text} is correct")
#     else:
#         line = get_hint(heart_sutra, 0)
#         click.echo(f"you typed")
#         click.echo(text)
#         click.echo("that line is")
#         click.echo(f"{line}")

