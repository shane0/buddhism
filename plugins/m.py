#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" mind ground """

import click
import os
import sys
import inspect
import pyperclip

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
def s():
    """show"""

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
