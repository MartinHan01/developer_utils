

# -*- coding:utf-8 -*-

"""the script to @ViewInject -> findViewById, @ContentView -> setContentView"""

import os
import re
import sys
from ClassData import ClassData



def write_new_file(arg_file, arg_line, data):
    trip_line = arg_line.strip()
    if trip_line.startswith('@ContentView'):
        return
    elif trip_line.startswith('@ViewInject'):
        return
    elif trip_line.startswith('@Event'):
        return 
    elif trip_line.startswith('super.onCreate('):
        arg_file.write(arg_line)
        first_word_index = arg_line.index('s')
        space = ''
        for index in range(first_word_index):
            space += ' '
        arg_file.write(space + data.get_content_view_string() + '\n')
        find_list = data.get_find_view_string()
        for line in find_list:
            arg_file.write(space + line + '\n')
        for key in data.event_dict.keys():
            arg_file.writelines(data.get_set_listener_lines(key, space))
    else:
        arg_file.write(arg_line)
    arg_file.flush()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('must has a work dir')
        exit()
    WORK_DIR = str(sys.argv[1])
    for dirpath, dirname, files in os.walk(WORK_DIR):
        for filename in files:
            absolute_path = os.path.join(dirpath, filename)
            if filename.endswith('Activity.java'):
            # if filename == 'FeedbackActivity.java' or filename == 'ChoosePaywayActivity.java':
            # if filename == 'MainActivity.java':
                new_file = open(os.path.join(dirpath, 'bak_' + filename), 'w', -1, encoding='utf-8')
                data = ClassData()
                previous_isid = False
                previous_is_event = False
                previous_event_id = ''
                file_fd = open(absolute_path, 'r+', -1, encoding='utf-8')
                while True:
                    line = file_fd.readline()
                    if not line:
                        break
                    old_line = str(line)
                    line = line.strip()
                    if not line:
                        new_file.write(old_line)
                        continue
                    if line.startswith('@ContentView'):
                        pattern = re.compile(r'\((.+?)\)') # find R.id.xxx
                        find = re.findall(pattern, line)
                        if find:
                            data.content_view = find[0]
                    elif line.startswith('@ViewInject'):
                        pattern = re.compile(r'\((.+?)\)') # find R.id.xxx
                        find = re.findall(pattern, line)
                        if find:
                            data.id_list.append(find[0])
                            previous_isid = True
                    elif line.startswith('@Event'):
                        pattern = re.compile(r'\((.+?)\)')
                        find = re.findall(pattern, line)
                        if find:
                            data.event_dict[find[0]] = ''
                            previous_event_id = find[0]
                            previous_is_event = True
                    elif previous_isid:
                        previous_isid = False
                        var_name = ''
                        type_name = ''
                        pattern = re.compile(r'\s(\w+?);')
                        find = re.findall(pattern, line)
                        if find:
                            var_name = find[len(find) - 1]
                        if re.match('^public|private|protected', str(line)):
                            type_pattern = re.compile(r'\s(\w+?)\s')
                            find_type = re.findall(type_pattern, line)
                        else:
                            type_pattern = re.compile(r'(\w+)\s')
                            find_type = re.findall(type_pattern, line)
                        type_name = find_type[0]
                        data.name_list.append(var_name)
                        data.type_list.append(type_name)
                        data.find_list.append('%s = (%s)findViewById(%s);' \
                            % (var_name, type_name, data.id_list[len(data.id_list) - 1]))
                        # print(data.find_list[len(data.find_list) - 1])
                    elif previous_is_event:
                        previous_is_event = False
                        pattern = re.compile(r'\s(\w+?)\(')
                        find = re.findall(pattern, line)
                        if find:
                            data.event_dict[previous_event_id] = find[0]
                file_fd.seek(0, os.SEEK_SET)
                new_file.seek(0, os.SEEK_SET)
                for line in file_fd:
                    write_new_file(new_file, line, data)
                    # print(line)
                new_file.flush()
                new_file.close()
                file_fd.close()
                os.remove(os.path.join(dirpath, filename))
                os.rename(os.path.join(dirpath, 'bak_' + filename), os.path.join(dirpath, filename))
                del data
                print(absolute_path)

