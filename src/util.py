from math import floor
import os, sys
from pystyle import Colorate, Colors


def clear_output():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def colorize(string):
    return Colorate.Vertical(Colors.yellow_to_red, string)


def indent(string, percent):
    rows = string.split("\n")
    longest_line = len(max(rows))
    result = ""

    for row in rows:
        spaces = " " * floor((os.get_terminal_size().columns - longest_line) * percent)

        result += spaces + row.strip() + "\n"

    return result


def out(string, center=False, color=False):
    final_string = string

    if center:
        final_string = ""

        for row in string.split("\n"):
            final_string += row.center(os.get_terminal_size().columns, " ")

    if color:
        final_string = colorize(final_string)

    print(final_string)


def set_title(terminal_title):
    out(f"\33]0;{terminal_title}\a")
