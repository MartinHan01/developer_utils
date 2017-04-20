#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
需要先安装xpinyin
pip install xpinyin
批量中文文件名转拼音

"""


from xpinyin import Pinyin
import os
import sys


def list_all(dir_name):
    pinyin_converter = Pinyin()
    for dirpath, dirnames, filenames in os.walk(dir_name):
        for filename in filenames:
            res = pinyin_converter.get_pinyin(filename, '_')
            res = res.replace('-', '')
            res = res.replace(' ','_')
            res = res.lower()
            if res[-5] == '_':
                res = res[:-5] + res[-4:]
            src_path = dirpath + '\\' + filename
            dest_path = dirpath + '\\' + res
            print(src_path + '->' + res)
            os.rename(src_path, dest_path)


if __name__ == '__main__':
    print(sys.argv)
    if sys.argv == 1:
        print('must has name dir')
        exit(-1)
    for dir_name in sys.argv[1:]:
        list_all(dir_name)


