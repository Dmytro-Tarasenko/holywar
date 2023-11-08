"""Answers the eternal question: what is better, or whoes kung-foo is stronger"""
from timeit import timeit
from dis import dis
from sys import argv
from io import StringIO
from contextlib import redirect_stdout
import argparse


def usage(error):
    """Prints instructions how to start HolyWar!!!"""
    print(f'{error}')

def demo():
    holywar('8.2 // 1', 'int(8.2)')
def holywar(*contestants, mode='full'):
    for contst in contestants:
        print(contst)
    print(mode)
    # with open(stdout.buffer.fileno())


def main():
    # Use a breakpoint in the code line below to debug your script.
    parser = argparse.ArgumentParser()
    parser.add_argument('-demo',
                        help='starts holywar: "8.2 // 1" vs "int(8.2)"')
    parser.add_argument('-s',
                        help='speed only matter')
    parser.add_argument('-d',
                        help='weird, but checks only whoes dissambly is shorter')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
