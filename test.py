
import re

if __name__ == '__main__':
    # pattern = re.compile(r'\((.+?)\)')
    # find = re.findall(pattern ,'@ViewInject(R.id.hello)')
    pattern = re.compile(r'\s(\w+?);')
    find = re.findall(pattern ,'public EditText mEt;')
    if find:
        print(find)
