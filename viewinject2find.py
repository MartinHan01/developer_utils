
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
            var_name = ''
            type_name = ''
            pattern = re.compile(r'\s(\w+?);')
            find = re.findall(pattern ,line)
            if find:
                var_name = find[len(find) - 1]
            else:
                continue
            if(re.match('^public|private|protected' ,line)):
                type_pattern = re.compile(r'\s(\w+?)\s')
                find_type = re.findall(type_pattern ,line)
            else:
                type_pattern = re.compile(r'(\w+)\s')
                find_type = re.findall(type_pattern ,line)
            type_name = find_type[0]
            if len(type_name) == 0:
                continue
            print(find)
            finds_res.append('%s = (%s)findViewById(%s);' % (var_name ,type_name ,resid))
            declarations.append(line)


    print()
    print('private void initView() {')
    for line in finds_res:
        print('    %s' % line)
    print('}')
    print()

    for line in declarations:
        print(line)
