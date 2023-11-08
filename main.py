"""Answers the eternal question: what is better, or whose kung-foo is stronger"""
from timeit import timeit
from dis import dis
from sys import argv
import os
from io import StringIO
from contextlib import redirect_stdout
#import argparse


def usage(error=''):
    """Prints instructions how to start HolyWar!!!"""
    print(f'\n{"There is no truth - only War, HolyWar!!! ":=^80}\n')
    if error:
        print(f"{error}'ve been just happend\n")
    print(f'Usage: {argv[0].split(os.path.sep)[-1]} <rival1> <rival2>',
          '[<rival3> <rival4>] [-s -a --demo]\n')
    print(f'{" ":<5}{"<rival_>":<10} rival codes for holywar',
          '(4 is ok, for more rivals make stages)')
    print(f'{" ":<5}{" ":<10} rival codes can be quoted codeblocks',
          'or pathes to files with codeblock')
    print(f'{" ":<5}{"-s":<10} only speed is really matters,',
           'who cares about anything else?')
    print(f'{" ":<5}{"-a":<10} wins rival with SHORTER disassembly',
          '(yeah, weird, but who we are to decide)')
    print(f'{" ":<5}{"--demo":<10} {argv[0].split(os.path.sep)[-1]}',
          '"8.2 // 1" "int(8.2)" simple battle with -s -a mean results')
    print(f'{error}')

def demo():
    holywar('8.2 // 1', 'int(8.2)')


def holywar(*contestants, mode='no-rules'):
    for contst in contestants:
        print(contst)
    print(mode)
    # with open(stdout.buffer.fileno())


def main():
    #Use a breakpoint in the code line below to debug your script.
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-demo',
    #                    help='starts holywar: "8.2 // 1" vs "int(8.2)"')
    #parser.add_argument('-s',
    #                    help='speed only matter')
    #parser.add_argument('-d',
    #                    help='checks only whose dissambly is shorter (yeah, it`s weird)')
    if len(argv) < 2:
        usage()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
