import sys
import io
import os

if __name__ == '__main__':
    if len(sys.argv) == 1:
        lines = []
        while True:
            try:
                line = input()
                if line:
                    lines.append(line)
            except EOFError:
                lines.append('\n')
                break

        text = '\n'.join(lines)
        file = io.StringIO(text)
    else:
        file = open(sys.argv[1])

    prefix = ('public' ,'protected' ,'private')
    for line in file:
        line = line.strip().lstrip()
        if line.startswith('@ViewInject'):
            




