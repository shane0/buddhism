#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" samu """

import click
import os
import sys
import inspect
import pyperclip
from plugins.mods.heart_sutra_text import heart_sutra
from plugins.mods.heart_sutra import (
    first_letter,
    get_hint,
    get_sutra_length,
    check_sutra_line,
    quiz,
    read_by_line,
    first_letters,
    read_by_line_short,
    get_random_line, 
    get_random_first_letter,
)


# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    samu
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def a():
    """anapanasati"""
    cmd = "curl https://shanenull.com/buddhism/2024/static/files/anapanasati"
    os.system(cmd)

@cli.command()
def e():
    """emotion"""
    cmd = "curl https://shanenull.com/buddhism/2024/static/files/emotion"
    os.system(cmd)

# fixme docs are confusing remove arg
# https://click.palletsprojects.com/en/8.1.x/api/#click.File
# trying to find out if there is a benefit to using click.file vs python read file
# @cli.command()
# def el():
#     """
#     read file with click
#     """
#     staticfile ='docs/static/files/emotiondata'
#     with click.argument('file_path', type=click.File('r'), default=f'{staticfile}') as f:
#         contents = f.read()
#         click.echo(contents)
    # with click.argument('file_path', type=click.File('r'), default='docs/static/files/emotiondata') as f:
    #     contents = f.read()
    #     click.echo(contents)

@cli.command()
@click.argument('file_path', type=click.File('r'), default='docs/static/files/emotion')
def el(file_path):
    """
    show emotion file locally
    """
    contents = file_path.read()
    click.echo(contents)

# ls docs/static/files/ | pbcopy
# anapanasati
# awakening
# awareness
# diamond_sutra
# emotion
# heart_sutra
# heart_sutra_first_letters
# path
# truths
# unanswerable
# winds

# @cli.command()
# def r():
#     """learn line by line using abbreviations"""
#     read_by_line(heart_sutra)


# @cli.command()
# def rs():
#     """read full lines with next line abbreviation"""
#     read_by_line_short(heart_sutra)


# @cli.command()
# def p():
#     """heart sutra practice typing each line - with abbreviations"""
#     quiz(heart_sutra)


# @cli.command()
# def w():
#     """heart sutra webpage"""
#     url = "https://shanenull.com/buddhism/2024/heart_sutra/"
#     click.launch(url)

# @cli.command()
# def c():
#     """colab heart sutra """
#     url = "https://colab.research.google.com/drive/1TLPkBWYqGA7Rk4g4fl9xFVLVdUA_1Da2"
#     click.launch(url)

# @cli.command()
# def s():
#     """show the entire heart sutra"""
#     # show
#     for h in heart_sutra:
#         click.echo(h)
#     # clipboard entire sutra 
#     result_string = "\n".join(heart_sutra)
#     pyperclip.copy(result_string)


# @cli.command()
# def f():
#     """show heart sutra first letters only"""
#     sutra_first_letters = first_letters(heart_sutra)
#     click.echo(sutra_first_letters)
#     pyperclip.copy(sutra_first_letters)

# @cli.command()
# def sfl():
#     """show heart sutra first letter of sentence"""
#     collect_first_letters = ""
#     for line in heart_sutra:
#         collect_first_letters += (first_letter(line))
#         # click.echo(first_letter(line))
#     click.echo(collect_first_letters)
#     pyperclip.copy(collect_first_letters)

# @cli.command()
# def l():
#     """show heart sutra length"""
#     length = get_sutra_length(heart_sutra)
#     click.echo(f"{length} lines")


# @cli.command()
# def rl():
#     """random line"""
#     random_line = get_random_line(heart_sutra)
#     click.echo(random_line)

# # todo: first letter has duplicates think about it 2 3 or ?
# # @cli.command()
# # def rf():
# #     """random first letter of line"""
# #     random_line = get_random_line(heart_sutra)
# #     click.echo(random_line)

# @cli.command()
# @click.option('--repeats', prompt='number of repeats', default=100)
# def rf(repeats):
#     """random first letters"""
#     for _ in range(repeats):
#         random_line = get_random_first_letter(heart_sutra)
#         click.echo(random_line)

