#!/usr/bin/env python
#
from dateutil import parser

date_strings = [  # <1>
    'February 1, 2021',
    '2/1/2021',
    '2/1/21',
    'Feb 1, 2021',
    'Feb 1 2021',
    'Feb 29, 2020',
    'Feb 29, 2021',
    'Feb 1 2021',
    '02/01/2021',
    '1 Feb 2021',
    'February 1st, 2021',
    'February 1, 2021 8:09',
    '2/1/2021 8:09 PM',
    'Feb 1, 2021 5 AM',
    'Febrifuge 1, 2021',
    '    2/1/21 13:45:19.233432      ',
    'abc 2/1/21',
]

for date_string in date_strings:
    print(f"{date_string:25s}", end=' ')
    try:
        dt = parser.parse(date_string)  # <2>
        print(dt)
    except ValueError as err:
        print(err)
