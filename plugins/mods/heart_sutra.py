#!/usr/bin/env python
# module for learning a sutra
import click


def prompt_user():
    text = click.prompt(text="enter sutra text")
    return text


def quiz(sutra_list):
    total_lines = get_sutra_length(sutra_list)
    correct_lines = 0

    for line_number in range(total_lines):
        click.echo(f"Line {line_number + 1} of {total_lines}")
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
