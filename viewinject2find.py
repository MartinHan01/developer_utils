
# -*- coding:utf-8 -*-

import sys
import io
import os
import re

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

    finds_res = []
    declarations = []
    for line in file:
        line = line.strip()
        if(line.startswith('@')):
            pattern = re.compile(r'\((.+?)\)')
            find = re.findall(pattern ,line)
            if find:
                resid = find[0]
        else:
            pattern = re.compile(r'\s(\w+?);')
            find = re.findall(pattern ,line)
            if find:
                var_name = find[len(find) - 1]
                finds_res.append('%s = findViewById(%s);' % (var_name ,resid))
                declarations.append(line)


    print()
    print('private void initView() {')
    for line in finds_res:
        print('    %s' % line)
    print('}')
    print()

    for line in declarations:
        print(line)
