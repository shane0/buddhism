#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" mind ground """

import click
import os
import sys
import inspect
import pyperclip
from plugins.mods.mind_ground_text import mind_ground
from plugins.mods.ox_text import oxherding_full_text
import plugins.mods.memorization as memorization

# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    mind ground
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")

@cli.command()
def os():
    """show the entire ox herding"""
    # show
    for h in oxherding_full_text:
        click.echo(h)
    # clipboard entire sutra 
    result_string = "\n".join(oxherding_full_text)
    pyperclip.copy(result_string)

@cli.command()
def o():
    """first letters oxherding """
    ox_first = memorization.first_letters(oxherding_full_text)
    click.echo(ox_first)
    pyperclip.copy(ox_first)
    # one line
    # test = memorization.shorten(ox_first)
    # click.echo(test)

@cli.command()
def f():
    """first letters mind ground"""
    mind_ground_text = memorization.first_letters(mind_ground)
    click.echo(mind_ground_text)
    pyperclip.copy(mind_ground_text)

@cli.command()
def c():
    """curl mind_ground"""
    cmd = "curl https://shanenull.com/buddhism/2024/static/files/mind_ground"
    os.system(cmd)

@cli.command()
def w():
    """workarounds"""
    text = """
bored --> maranasati or buddha statue
sleepy --> count breath
scattered--> follow breath
"""
    click.echo(text)

@cli.command()
def ws():
    """web"""
    urls = [
        "https://shanenull.com/buddhism/2024/mind_ground/",
        "https://ctworld.org/Buddhist%20e-Books/Audio/Book007/index.html"
    ]
    for u in urls:
        click.launch(u)
