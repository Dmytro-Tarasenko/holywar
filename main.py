"""Answers the eternal question: what is better, or whose kung-foo is stronger"""
from timeit import timeit
from dis import dis
from sys import argv
import os
from pathlib import Path
from io import StringIO
from contextlib import redirect_stdout
from rich.console import Console
from rich.table import Table

def disclaimer():
    """Prints disclaimer"""
    print(f'{"!!!DISCLAIMER!!!":^60}\n',
          '\tThe main purpose of holywar is to entertain people rather \n',
          'than arguing about which one of code block or programing \n',
          'technique is better. It is strongly recommended to consider \n',
          'that actual code is being executed during holywar so use only\n',
          'trusted sources of rival codes and under any circumstances \n',
          'DO NOT upload rival codes from the Internet especially from \n',
          'unknown or untrusted sources!\n',
          'Holywar is provided AS IS with no warranty or liability.\n')


def usage(error=''):
    """Prints instructions how to start HolyWar!!!"""
    print(f'\n{"There is no truth - only War, HolyWar!!! ":=^80}\n')
    if error:
        print(error)
    print(f'Usage: {argv[0].rsplit(os.path.sep, maxsplit=1)[1]} <rival1> <rival2>',
          '[<rival3> <rival4>] [-s -a --demo]\n')
    print(f'{" ":<5}{"<rival_>":<10} rival codes for holywar',
          '(4 is ok, for more rivals make stages)')
    print(f'{" ":<5}{" ":<10} rival codes can be quoted codeblocks',
          'or pathes to files with codeblock or their mixes')
    print(f'{" ":<5}{"-s":<10} only speed is really matters,',
          'who cares about anything else?')
    print(f'{" ":<5}{"-a":<10} wins rival with SHORTER disassembly',
          '(yeah, weird, but who we are to decide)')
    print(f'{" ":<15} if no rules (-s or -a) are specified',
          'rival with better mean result wins')
    print(f'{" ":<5}{"--demo":<10} {argv[0].rsplit(os.path.sep, maxsplit=1)[1]}',
          '"8.2 // 1" "int(8.2)" simple battle with -s -a mean results')
    print(f'{error}')


def demo():
    """Runs demonstration of holy-war with rivals 8.2 // 1 and int(8.2)"""
    holywar(['8.2 // 1', 'int(8.2)'], mode='no-rules')


def holywar(rivals, mode='no-rules'):
    """Does its main job, computes, gathers, displays"""
    results = []
    if len(rivals) == 1:
        print(f'{"!!!!Flawless Brutal Fatality!!!!":^60}')
        rival_txt = rivals[0] if len(rivals[0]) <= 15 \
            else rivals[0][:15]+'...'
        print(f'Rival #1: "{rival_txt}" wins! '
              + 'Condition 1st place from 1 contestant!')
        return 0
    rival_ind = 1
    for code in rivals:
        rival_txt = code if len(code) <= 12 else code[:12] + '...'
        rival_title = f'Rival #{rival_ind}'
        with redirect_stdout(StringIO()) as fout:
            dis(code)
            rival_speed = timeit(code, number=1000000)
        rival_asm = len(fout.getvalue().split('\n'))
        results.append({'title': rival_title,
                        'text': rival_txt,
                        '-s': rival_speed,
                        '-a': rival_asm,
                        'no-rules': (rival_speed+rival_asm/100)/2})
        rival_ind += 1
    results.sort(key=lambda i: i[mode])
    appndx = ''
    for i in range(1, len(results)):
        worther = (results[i][mode]/results[0][mode])*100
        appndx += f'{' ':<5}place #{i+1} {results[i]['title']}: "{results[i]['text']}" '
        appndx += f'with the result: {results[i][mode]:.9f} - {worther:.2f}% worther'
    print(f'The WINNER is {results[0]['title']}: "{results[0]['text']}"',
          f'with the result: {results[0][mode]:.9f}')
    print(appndx)
    return 0


# def display_results(results):
#     """Display result of holy-war"""
#     if len(results) == 0:
#         print(f'{r"\_()_/":^60}')
#         print(f'{"Got no results to display":^60}')
#         return 0
#     console = Console()
#     table = Table(title='Final results', title_justify='center', title_style='bold red',
#                   show_header=True, header_style='blue')
#     table.add_column(r'Feature\Results')
#     for _ in results:
#         table.add_column(_)
#     console.print(table)


def validate_rival(rival):
    """Checks for valid Python code block or file
    with valid python code"""
    error = ''

    try:
        with redirect_stdout(StringIO()) as _:
            timeit(rival, number=1)
    except:
        rival_txt = rival if len(rival) <= 12 else rival[:12] + '...'
        error = f'"{rival_txt}" is not a valid rival code'
    if error == '':
        return rival, error

    if Path(rival).is_file():
        with open(rival, 'r', encoding='utf-8') as fin:
            pretender = ''.join(fin.readlines())
        try:
            with redirect_stdout(StringIO()) as _:
                timeit(pretender, number=1)
            rival = pretender
            error = ''
        except:
            error = f'{error.replace("not", "neither")},' \
                    + ' nor a file with a valid code'
            rival = ''

    return rival, error


def main():
    """Provides initial args check, prepares parameters and rivals,
    passes them to holy-war"""
    disclaimer()
    mode = 'no-rules'
    rivals = []

    if len(argv) < 2:
        usage()
    if '-s' in argv and '-a' in argv:
        mode = 'no-rules'
        argv.pop(argv.index('-s'))
        argv.pop(argv.index('-a'))
    if '-s' in argv:
        mode = '-s'
        argv.pop(argv.index('-s'))
    if '-a' in argv:
        mode = '-a'
        argv.pop(argv.index('-a'))

    if '--demo' in argv:
        holywar(['8.2 // 1', 'int(8.2)'])
        return 0

    for arg in argv[1:]:
        rival, error = validate_rival(arg)
        if error:
            print(error)
            continue
        rivals.append(rival)

    if len(rivals) == 0:
        usage('No valid rival codes were provided.')

    if len(rivals) > 4:
        print('==>(4 is ok, for more rivals make stages)<==')
        rivals = rivals[:4]

    holywar(rivals, mode=mode)
    return 0


if __name__ == '__main__':
    main()
