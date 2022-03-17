#!/usr/bin/env python

import re

s = """lorem ipsum M-302 dolor sit amet, consectetur r-99 adipiscing elit, sed do
 eiusmod tempor incididunt H-476 ut labore et dolore magna Q-51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z-883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A-110 cupidatat non proident, sunt in H-332 culpa qui 
officia deserunt Y-45 mollit anim id est laborum"""

#   tob(?:y|ey|ie)

#
#           0
#           -----------------
#           1       2
#           ------- ---------
pattern = r'([A-Z])-(\d{2,3})'  # <1>

for m in re.finditer(pattern, s):
    print(m.group(0), m.group(1), m.group(2))  # <2>
    print(m.start(1), m.end(1), m.span())
    print('-' * 60)
print()

matches = re.findall(pattern, s)  # <3>
print("matches:", matches)

mac_addresses = [
    "5A:72:35:13:51:3F",
    "E6:C2:D5:55:96:BC",
    "A2:27:CD:E5:00:7F",
    "FD881C47F3A5",
    "E5:AD:20:D6:DF:B1",
    "5A:72:35:13:51:3F",
    "5A723513513F",
    "A227CDE5007F",
    "D6:3F:80:35:41:4A",
]

rx_mac = r"([0-9a-f]{2}):?([0-9a-f]{2}):?([0-9a-f]{2}):?([0-9a-f]{2}):?([0-9a-f]{2}):?([0-9a-f]{2})"

unique_macs = set()

for mac in mac_addresses:
    for m in re.finditer(rx_mac, mac, re.I):
        unique_macs.add(m.groups())


for mac in sorted(unique_macs):
    print(mac)


# "\d+(?st|nd|rd|th)(?=\s+street)"  # lookahead
