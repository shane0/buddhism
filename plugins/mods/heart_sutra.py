#!/usr/bin/env python
# module for learning a sutra
import click
import random


def validate_non_empty_string(string):
    if not isinstance(string, str):
        raise TypeError("Parameter must be a string")
    if not string:
        raise ValueError("String cannot be empty")
    return True


def first_letters(sentences):
    """Returns a string of the first letters of each word in a list of sentences, separated by dashes.

    Args:
      sentences: A list of sentences.

    Returns:
      A string containing the first letters of each word in each sentence, separated by dashes.
    """

    result = ""
    for sentence in sentences:
        first_letters = "".join(word[0] for word in sentence.split())
        result += f"{first_letters}-"
    return result[:-1]  # Remove the trailing dash


def prompt_user():
    text = click.prompt(text="enter sutra text")
    return text


def first_letters(sentences):
    """Returns a string of the first letters of each word in a list of sentences, separated by newlines.

    Args:
      sentences: A list of sentences.

    Returns:
      A string containing the first letters of each word in each sentence, separated by newlines.
    """

    result = ""
    for sentence in sentences:
        first_letters = "".join(word[0] for word in sentence.split())
        result += f"{first_letters}\n"
    return result[:-1]  # Remove the trailing newline


def shorten(text):
    """Returns a string containing the first letter of each word in the given text.

    Args:
      text: The input text.

    Returns:
      A string containing the first letter of each word.
    """
    validate_non_empty_string(text)

    return "".join(word[0] for word in text.split())


def read_by_line(sutra_list):
    if not isinstance(my_list, list):
        raise TypeError("my_list must be a list")
    total_lines = get_sutra_length(sutra_list)
    next_line = 1
    for line_number in range(total_lines):
        hint = get_hint(sutra_list, line_number)
        next_hint = shorten(sutra_list[next_line])
        click.echo(hint)
        click.echo(next_hint)
        click.confirm(text="enter to continue")
        next_line += 1


def read_by_line_short(sutra_list):
    total_lines = get_sutra_length(sutra_list)
    next_line = 1
    for line_number in range(total_lines):
        big_hint = get_hint(sutra_list, line_number)
        hint = shorten(sutra_list[line_number])
        # click.echo(hint)
        click.echo(big_hint)
        next_hint = shorten(sutra_list[next_line])
        click.echo(next_hint)
        click.confirm(text="enter to continue")
        next_line += 1


def quiz(sutra_list):
    total_lines = get_sutra_length(sutra_list)
    correct_lines = 0

    for line_number in range(total_lines):
        click.echo(f"Line {line_number + 1} of {total_lines}")
        # hint mode full line
        # hint = get_hint(sutra_list, line_number)
        # hint mode first letter
        hint = shorten(sutra_list[line_number])
        click.echo(hint)
        while True:
            user_input = prompt_user()

            if check_sutra_line(sutra_list, line_number, user_input):
                click.echo("Correct!")
                correct_lines += 1
                break
            else:
                click.echo(
                    f"Incorrect. The correct line was: '{sutra_list[line_number]}'"
                )
                retry = click.confirm("Do you want to try again?", default=True)
                if not retry:
                    break

    if correct_lines == total_lines:
        click.echo("Congratulations! You have correctly typed all lines.")
    else:
        click.echo(f"You typed {correct_lines}/{total_lines} lines correctly.")


def get_sutra_length(sutra_list):
    return len(sutra_list)


def get_hint(sutra_list, index):
    try:
        return sutra_list[index]
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Invalid index type"


def check_sutra_line(sutra_list, line_number, text):
    try:
        return sutra_list[line_number] == text
    except IndexError:
        return False
    except TypeError:
        return False


def get_random_line(sutra_list):
    total_lines = get_sutra_length(sutra_list)
    random_index = random.randrange(0, total_lines)
    return sutra_list[random_index]


def get_random_first_letter(sutra_list):
    total_lines = get_sutra_length(sutra_list)
    random_index = random.randrange(0, total_lines)
    click.echo(shorten(sutra_list[random_index]))
    if click.confirm(text="show", default=True):
        click.echo(sutra_list[random_index])
