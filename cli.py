#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cli.py
"""shane null command line workflows"""
import click
import os
import logging
import inspect
import sys
import shutil
import datetime
import sys

import sys



plugin_folder = os.path.join(os.path.dirname(__file__), "plugins")
homedir = os.path.expanduser("~")
TODAY = datetime.date.today().strftime("%Y-%m-%d")
ISODATE = datetime.date.today().strftime("%Y-%m-%d")
ISOFILE = ISODATE + ".md"
BUJO_FOLDER = os.path.join(os.path.dirname(__file__), "docs/bujo")
MONTH = datetime.date.today().strftime("%m_%B")
WEEK = datetime.date.today().strftime("%U")
DAYFILE = BUJO_FOLDER + "/" + TODAY + ".md"
WEEKFILE = BUJO_FOLDER + "/" + WEEK + ".md"
MONTHFILE = BUJO_FOLDER + "/" + MONTH + ".md"
YEAR = datetime.date.today().strftime("%Y")


# Set up the logger
from plugins.mods.log_tools import setup_logger
# logger = setup_logger('cli_logger', logging.DEBUG)
logger = setup_logger(logging.DEBUG)


# logger = setup_logger('cli_logger', logging.DEBUG)

# # Example usage of logging
# def main():
#     logger.debug('This is a debug message from the CLI.')
#     logger.info('This is an info message from the CLI.')
#     logger.warning('This is a warning message from the CLI.')
#     logger.error('This is an error message from the CLI.')
#     logger.critical('This is a critical message from the CLI.')

# if __name__ == "__main__":
#     main()


# Define the log file path in the plugins/ directory
# log_directory = "plugins/logs"
# os.makedirs(log_directory, exist_ok=True)  # Create the 'logs' directory if it doesn't exist
# log_file = os.path.join(log_directory, "cli_commands.log")

# # Set up the logger to log to a file
# logging.basicConfig(
#     level=logging.INFO,  # Adjust level as needed (DEBUG, INFO, WARNING, etc.)
#     format="%(asctime)s - %(levelname)s - %(message)s",  # Customize log format
#     handlers=[
#         logging.FileHandler(log_file, mode='a'),  # Append to log file instead of overwriting
#         logging.StreamHandler()  # Also print logs to the console
#     ]
# )
# logger = logging.getLogger(__name__)


class PluginCLI(click.MultiCommand):
    def list_commands(self, ctx):
        """Dynamically get the list of commands."""
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and not filename.startswith("__init__"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Dynamically get the command."""
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        try:
            with open(fn) as f:
                code = compile(f.read(), fn, "exec")
                eval(code, ns, ns)
            logger.info(f"cli.py {name} loaded successfully.")  # Log successful command loading
        except Exception as e:
            logger.error(f"Error loading cli.py {name}: {e}")
        
        # Return the dynamically loaded command
        command = ns.get("cli")
        if command:
            if len(sys.argv) > 1:
                logger.info(f"cli.py {sys.argv[1]}")
                if len(sys.argv) > 2:
                    logger.info(f"cli.py {sys.argv[1]} {sys.argv[1]}")
                logger.info(f"Loading command: {name}")  # Log the command being loaded
            # Access before_invoke directly
            # logger.info(f"cli.py '{ctx.command.name}' executed with arguments: {ctx.args}")
            return command
        # return command

# fix me this does not log the 2nd argument
# 2024-12-09 18:13:46,469 - INFO - Starting the CLI application...
# 2024-12-09 18:13:46,470 - INFO - Loading command: bujo
# 2024-12-09 18:13:46,475 - INFO - Command bujo loaded successfully.
# 2024-12-09 18:13:46,475 - INFO - Command 'cli' executed with arguments: []
import pdb

def before_invoke(self, ctx):
    if len(sys.argv) > 1:
        logger.info(f"cli.py {sys.argv[1]}")
        if len(sys.argv) > 2:
            logger.info(f"cli.py {sys.argv[1]} {sys.argv[1]}")
        logger.info(f"Loading command: {name}")  # Log the command being loaded
    click.echo(f"Arguments: {ctx.args}")

# def before_invoke(self, ctx):
#     print(f"Arguments: {ctx.args}")
#     logger.info(f"Command '{ctx.command.name}' executed with arguments: {ctx.args}")
# def before_invoke(self, ctx):
#     pdb.set_trace()  # Set a breakpoint here
#     args = ctx.args
#     logger.info(f"Command '{ctx.command.name}' executed with arguments: {args}")
# def before_invoke(self, ctx):
#     args = ctx.params.values()
#     logger.info(f"Command '{ctx.command.name}' executed with arguments: {args}")

# def before_invoke(self, ctx):
#     args = ctx.args
#     if len(args) >= 2:
#         command = args[0]
#         argument = args[1]
#         logger.info(f"Executing command '{command}' with argument '{argument}'")

@click.command(cls=PluginCLI)
def cli():
    """2022 Shane Null Workflows"""
    pass

if __name__ == "__main__":

    cli()
