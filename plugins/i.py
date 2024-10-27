#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""impermenence"""

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
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import requests
import json

def fetch_and_display_data(url):
  """Fetches JSON data from the provided URL, handling potential CORS issues,
  and displays the keys and values in a user-friendly format.
  """

  # Replace with a CORS-handling proxy service URL if needed
  proxy_url = None  # "https://cors-anywhere.herokuapp.com/"  # uncomment if necessary


  try:
    # Send the GET request with optional CORS proxy
    if proxy_url:
      response = requests.get(url, proxies={"http": proxy_url, "https": proxy_url})
    else:
      response = requests.get(url)

    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Parse the JSON response
    data = response.json()

    # Display the keys and values in a clear format
    print("Data from", url)
    for key, value in data.items():
      print(f"  - Key: {key}")
      print(f"    Value: {value}")
      print()  # Add a new line for better readability

  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Call the function to execute the request and display data
# fetch_and_display_data()

@click.group()
def cli(args=None):
    """\b
    impermenence
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def h():
    """help"""
    help_text = """
ponlop recommends learning compassion then impermanence?
"""
    click.echo(help_text)

@cli.command()
def u():
    """urls"""
    urls = [
        # playlist
        "https://www.youtube.com/playlist?list=PLGY2UhH7nNtJWqAFSsyB02uysHtP2c-9d"
    ]
    for u in urls:
        click.launch(u)


@cli.command()
def f():
    """fetch api days"""
    url = "https://cors-shane0.vercel.app/api/day"
    fetch_and_display_data(url)
    # https://cors-shane0.vercel.app/api/day
