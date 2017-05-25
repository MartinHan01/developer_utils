

# -*- coding:utf-8 -*-

import os
import re
import sys
import io

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('must has a work dir')
        exit()
    WORK_DIR = str(sys.argv[1])
    for dirpath, dirname, files in os.walk(WORK_DIR):
        for filename in files:
            absolute_path = os.path.join(dirpath, filename)
            if filename.endswith('FeedbackActivity.java'):
                name_list = []
                type_list = []
                id_list = []
                find_list = []
                previous_isid = False
                file_fd = open(absolute_path, 'r+', -1, encoding='utf-8')
                while True:
                    line = file_fd.readline()
                    if not line:
                        break
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith('@ViewInject'):
                        pattern = re.compile(r'\((.+?)\)') # find R.id.xxx
                        find = re.findall(pattern, line)
                        if find:
                            id_list.append(find[0])
                            print('当前位置:%s' % file_fd.tell())
                            file_fd.seek(file_fd.tell(), os.SEEK_SET)
                            
                            file_fd.write('\n//hello world\n')
                            file_fd.flush()
                            previous_isid = True
                    elif previous_isid:
                        previous_isid = False
                        var_name = ''
                        type_name = ''
                        pattern = re.compile(r'\s(\w+?);')
                        find = re.findall(pattern, line)
                        if find:
                            var_name = find[len(find) - 1]
                        else:
                            continue
                        if re.match('^public|private|protected', str(line)):
                            type_pattern = re.compile(r'\s(\w+?)\s')
                            find_type = re.findall(type_pattern, line)
                        else:
                            type_pattern = re.compile(r'(\w+)\s')
                            find_type = re.findall(type_pattern, line)
                        type_name = find_type[0]
                        if not type_name:
                            continue
                        name_list.append(var_name)
                        type_list.append(type_name)
                        find_list.append('%s = (%s)findViewById(%s);' \
                            % (var_name, type_name, id_list[len(id_list) - 1]))
                        print(find_list[len(find_list) - 1])
                    # print(line)

                file_fd.close()
                print(absolute_path)

