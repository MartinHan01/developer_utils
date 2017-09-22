
# -*- coding:utf-8 -*-

import sys
import io
import os
import re

if __name__ == '__main__':
    if len(sys.argv) == 1:
        LINES = []
        while True:
            try:
                LINE = input()
                if str(LINE) == 'exit':
                    break
                if LINE:
                    LINES.append(LINE)
            except EOFError:
                LINES.append('\n')
                break

        TEXT = '\n'.join(LINES)
        FILE = io.StringIO(TEXT)
    else:
        FILE = open(sys.argv[1])

    FIND_RES = []
    DECLARATIONS = []
    for LINE in FILE:
        LINE = LINE.strip()
        if LINE.startswith('@'):
            pattern = re.compile(r'\((.+?)\)')
            find = re.findall(pattern, LINE)
            if find:
                resid = find[0]
        else:
            var_name = ''
            type_name = ''
            pattern = re.compile(r'\s(\w+?);')
            find = re.findall(pattern, LINE)
            if find:
                var_name = find[len(find) - 1]
            else:
                continue
            if re.match('^public|private|protected', str(LINE)):
                type_pattern = re.compile(r'\s(\w+?)\s')
                find_type = re.findall(type_pattern, LINE)
            else:
                type_pattern = re.compile(r'(\w+)\s')
                find_type = re.findall(type_pattern, LINE)
            type_name = find_type[0]
            if len(type_name) == 0:
                continue
            # print(find)
            FIND_RES.append('%s = (%s)findViewById(%s);' % (var_name, type_name, resid))
            DECLARATIONS.append(LINE)


    print()
    print('private void initView() {')
    for LINE in FIND_RES:
        print('    %s' % LINE)
    print('}')
    print('')

    for LINE in DECLARATIONS:
        print(LINE)
