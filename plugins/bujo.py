#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bullet journaling"""

from cli import (
    BUJO_FOLDER,
    ISODATE,
    ISOFILE,
    # MONTH,
    # WEEK,
    MONTHFILE,
    DAYFILE,
    WEEKFILE,
    YEAR,
)
import click

# import subprocess
import os
import sys
import inspect

# import glob
# import datetime

# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    bullet journaling & todocli
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def m():
    """start mkdocs server"""
    click.launch('http://localhost:8001')
    os.system('mkdocs serve')


@cli.command()
def s():
    """start dev server"""
    os.system('npm start')


@cli.command()
def m():
    """mkdocs serve"""
    click.launch("http://localhost:8002/")
    os.system("mkdocs serve")


@cli.command()
def s():
    """start dev server"""
    os.system("npm start")


@cli.command()
def ww():
    """weather"""
    os.system("curl wttr.in")


@cli.command()
def snip():
    """open snippet maker"""
    click.launch("https://snippet-generator.app/")


@cli.command()
def index():
    """bujo index file"""
    click.edit(filename="docs/bujo/index.md", editor="code")


@cli.command()
def future():
    """bujo index file"""
    click.edit(filename="docs/bujo/future.md", editor="code")


@cli.command()
def month():
    """month file"""
    click.echo(MONTHFILE)
    click.edit(filename=MONTHFILE, editor="code")


YEARFILE = BUJO_FOLDER + "/" + YEAR + ".md"


@cli.command()
def year():
    """week - cps state rollback test"""
    click.echo(YEARFILE)
    click.edit(filename=YEARFILE, editor="code")
    # click.edit(filename=YEARFILE)


@cli.command()
def week():
    """week - cps state rollback test"""
    click.echo(WEEKFILE)
    click.edit(filename=WEEKFILE, editor="code")


@cli.command()
def day():
    """week - cps state rollback test"""
    click.echo(DAYFILE)
    click.edit(filename=DAYFILE, editor="code")


@cli.command()
@click.option("--folder", prompt="folder /projectpath/")
def todo(folder):
    """generic todo"""
    try:
        home = os.path.expanduser("~")
        click.echo(home)
        folder = os.path.join(home, folder)
        click.echo(folder)
        os.chdir(folder)
        cmd = "./todocli/todo.sh ls"
        os.system(cmd)
    except OSError as err:
        click.echo("OS error: {0}".format(err))


@cli.command()
@click.argument("out", type=click.File("r"))
def read(out):
    """read a bujo/ file"""
    try:
        #        os.chdir(meditationfolder)
        click.echo(out.name)
        for x in out.readlines():
            click.echo(x)
    except OSError as err:
        click.echo("OS error: {0}".format(err))


@cli.command()
def remote():
    """jobs on remotive"""
    click.launch(
        "https://remotive.io/?live_jobs%5Bquery%5D=support%20engineer&live_jobs%5BrefinementList%5D%5Bquick_location_filter%5D%5B0%5D=USA%20Only"
    )

@cli.command()
def zl():
    """markdownlint"""
    cmd = "npx markdownlint 'docs/*.md' --config .markdownlint.json"
    os.system(cmd)


# pyperclip isn't working on pixelbook
# @cli.command()
# def link():
#    """linktree"""
#    url = "https://linktr.ee/shanenull"
#    pyperclip.copy(url)
#    try:
#        cmd = url + ' | xclip'
#        os.system(cmd)
#        click.echo(cmd)
#    except OSError as err:
#        click.echo("OS error: {0}".format(err))
#    if click.confirm("open linktree?"):
#        click.launch("https://linktr.ee/shanenull")


# @cli.command()
# def doing():
#     """todo doing"""
#     try:
#         cmd = "docs/bujo/todocli/todo.sh listpri a"
#         os.system(cmd)
#     except OSError as err:
#         click.echo("OS error: {0}".format(err))


# @cli.command()
# def trytis():
#     """try https://github.com/click-contrib"""
#     click.launch("https://github.com/click-contrib")


# @cli.command()
# def index():
#     """bujo index file"""
#     click.edit(filename="docs/bujo/index.md")


# @cli.command()
# def future():
#     """bujo index file"""
#     click.edit(filename="docs/bujo/future.md", editor="code")


@cli.command()
def folder():
    """create bujo folder"""
    try:
        cmd = "mkdir bujo"
        os.system(cmd)
        click.echo("mkdir bujo")
    except OSError as err:
        click.echo("OS error: {0}".format(err))


# @cli.command()
# def month():
#     """month"""
#     click.edit(filename='docs/bujo/"$(date +%m)"-"$(date +%B)".md', editor="code")


# @cli.command()
# def week():
#     """week"""
#     click.echo(WEEK)
#     click.edit(filename=f"docs/bujo/{WEEK}.md", editor="code")


# @cli.command()
# def day():
#     """day"""
#     click.edit(filename='docs/bujo/"$(date +%F)".md', editor="code")


# @cli.command()
# @click.option("--pattern", prompt="search term")
# def search(pattern):
#     """grep text in ./bujo and copy to clipboard"""
#     cmd = r"grep -r -2 %s ./bujo | cut -d':' -f 2 | sort -u" % pattern
#     result = subprocess.check_output(cmd, shell=True)
#     try:
#         pyperclip.copy(str(result))
#     except:
#         click.echo("no pyperclip for you")
#     if result:
#         click.echo(result)
#     else:
#         click.echo("grep found nada")


# this is an old snippet for demonstration of using python dates vs bash
@cli.command()
def dayfolder():
    """create subfolder with named todays date"""
    folderpath = os.path.join(BUJO_FOLDER, ISODATE)
    filepath = os.path.join(BUJO_FOLDER, ISODATE, ISOFILE)
    click.echo(BUJO_FOLDER)
    click.echo(folderpath)
    click.echo(filepath)
    if not os.path.exists(folderpath):
        os.mkdir(folderpath)
    if not os.path.exists(filepath):
        f = open(filepath, "a")
        f.write("# " + ISODATE)
        f.write("\n")
        f.write("\n")
        f.write("> " + BUJO_FOLDER)
        f.close()
    click.echo("folder for today created")


# sncli bujo open - example from cutters
# @cli.command('deploy')
# @click.option('--name',prompt='cookiecutter name',default='cookiecutter-project')
# @click.option('--output_folder',prompt='output folder',default=HOME_TEST)
# def deploy(name,output_folder):
#     """ deploy - deploys <cookiecutter> """
#     click.echo('searching %s for %s' % (COOKIECUTTER_FOLDER,name))
#     search_name = '*' + name + '*'
#     matches = glob.glob((COOKIECUTTER_FOLDER + '/' + search_name))
#     if len(matches) > 1:
#         click.echo('multiple matches found - choose one')
#         for m in matches:
#             if click.confirm('%s' % m):
#                 dirs = os.path.basename(m)
#                 shortname = dirs.replace('\'','')
#                 os.system('cookiecutter ' + shortname + ' -o ' + output_folder)
#     elif len(matches) == 1:
#         dirs = [os.path.basename(x) for x in matches]
#         name = dirs[0].replace('\'','')
#         args = ['cookiecutter ', name,' -o ',output_folder]
#         click.echo(args)
#         os.system('cookiecutter ' + name + ' -o ' + output_folder)
#         #subprocess.check_call(args)
#     else:
#         click.echo('%s - returned 0 results' % search_name)
# @cli.command()
# def oldmonth():
#    """bullet journal - monthly journal"""
#    try:
#        cmd = 'cd bujo && mkdir "$(date +%m)"-"$(date +%B)" && \
#                cd "$(date +%m)"-"$(date +%B)" && \
#                vim ./"$(date +%m)"-"$(date +%B)".md || \
#                cd "$(date +%m)"-"$(date +%B)" vim ./"$(date +%m)"-"$(date +%B)".md'
#        os.system(cmd)
#    except OSError as err:
#        click.echo("OS error: {0}".format(err))

# @cli.command()
# def oldday():
#    """bullet journal - todays journal"""
#    try:
#        cmd = 'cd bujo && touch "$(date +%F)".md && vim ./"$(date +%F)".md'
#        os.system(cmd)
#    except OSError as err:
#        click.echo("OS error: {0}".format(err))
