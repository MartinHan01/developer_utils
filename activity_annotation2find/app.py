
import os
import io
import sys


if __name__ == '__main__':
    if(len(sys.argv) == 1):
        print('must has a work dir')
        exit()
    work_dir = sys.argv[1]
    for dirpath, dirname, files in os.walk(work_dir):
        for filename in files:
            absolute_path = os.path.join(dirpath, filename)
            print(absolute_path)
