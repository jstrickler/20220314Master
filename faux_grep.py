import sys
import re
import fileinput
from argparse import ArgumentParser

#  -i -n  regex  file1 ...
parser = ArgumentParser(description="""
Faux grep

Print lines matching regex from one or more files. 

usage: grep -i -n -c -h regex file1 ...
""")

parser.add_argument("-i", dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument("-n", dest="show_name", action="store_true", help="show file name")
parser.add_argument("-c", dest="count_only", action="store_true", help="just count lines")
parser.add_argument("pattern", help="pattern to find")
parser.add_argument("files", nargs="*", help="files to search")

args = parser.parse_args()
print(args)

regex = re.compile(args.pattern, re.I if args.ignore_case else 0)

count = 0
for raw_line in fileinput.input(args.files):
    if regex.search(raw_line):
        if args.count_only:
            count += 1
        else:
            line = raw_line.rstrip()
            if args.show_name:
                print(fileinput.filename(), end=": ")
            print(line)
print("total lines: {}".format(count))