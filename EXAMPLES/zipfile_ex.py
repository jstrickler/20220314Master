#!/usr/bin/env python

from zipfile import ZipFile, ZIP_DEFLATED
import os.path

# reading & extracting
rzip = ZipFile("../DATA/textfiles.zip")  # <1>
print(rzip.namelist())  # <2>
ty = rzip.read('tyger.txt').decode()  # <3>
print(ty[:50])
rzip.extract('parrot.txt')  # <4>

# creating a zip file
wzip = ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED)  # <5>
for file_name in "parrot.txt tyger.txt knights.txt alice.txt poe_sonnet.txt spam.txt".split():
    file_path = os.path.join("../DATA", file_name)
    print("adding {}".format(file_path))
    wzip.write(file_path, file_name)  # <6>


