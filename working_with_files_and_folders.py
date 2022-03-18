import os
from datetime import datetime
from humanize import naturalsize

folder = "DATA"
file_name = "alice.txt"

file_path = os.path.join(folder, file_name)
print("file_path: {}\n".format(file_path))

folder_name = os.path.dirname(file_path)
base_name = os.path.basename(file_path)
print("folder_name: {}".format(folder_name))
print("base_name: {}\n".format(base_name))

file_base, file_extension = os.path.splitext(file_path)
print("file_base: {}".format(file_base))
print("file_extension: {}".format(file_extension))
new_name = file_base + '.csv'
print("new_name: {}\n".format(new_name))

print("os.path.isfile(file_path): {}".format(os.path.isfile(file_path)))
print("os.path.isdir(file_path): {}\n".format(os.path.isdir(file_path)))

for file_name in 'foo', 'bar', 'DATA/wombat.txt', 'DATA/presidents.txt', 'presidents.txt':
    print(file_name, os.path.exists(file_name))
print()

raw_ts = os.path.getmtime(file_path)
print("raw_ts: {}".format(raw_ts))
file_ts = datetime.fromtimestamp(raw_ts)
print("file_ts: {}\n".format(file_ts))

file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))

stat_info = os.stat(file_path)
print("oct(stat_info.st_mode): {}\n".format(oct(stat_info.st_mode)))
print("stat_info: {}\n".format(stat_info))

data_files = os.listdir('DATA')
print("data_files: {}\n".format(data_files))

text_files = [f for f in os.listdir('DATA') if f.endswith('.txt')]
print("text_files: {}\n".format(text_files))

total = 0
for file_name in text_files:
    file_path = os.path.join('DATA', file_name)
    file_size = os.path.getsize(file_path)
    natural_size = naturalsize(file_size)
    print(f"{natural_size:10s} {file_name}")
    total += file_size
print('-' * 60)
natural_total = naturalsize(total)
print(f"{natural_total:10s} TOTAL")
print('\n')

for entry in os.scandir('DATA'):
    print(entry.name, entry.is_file(), entry.is_dir())
