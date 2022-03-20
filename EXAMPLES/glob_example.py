#!/usr/bin/env python
# from module import function/class/data
from glob import glob

files = glob('../DATA/*.txt') # <1>
print(files, '\n')

no_files = glob('../DATA/*.avi')
print(no_files, '\n')

