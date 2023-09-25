import sys
import termcolor
from colorama import init, AnsiToWin32

init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


def print_hello():
    print(termcolor.colored('Hello termcolor', 'yellow'))


def print_hi():
    print(termcolor.colored('Hi, termcolor', 'red'))


if __name__ == "__main__":
    print_hello()

print_hi()
