import os
from datetime import datetime

starting_folder = os.path.abspath('.')

for folder, folders, file_names in os.walk(starting_folder):
    if ".git" in folders:
        folders.remove('.git')
    if folder.endswith("__"):
        continue
    print(folder)
    now = datetime.now()
    for file_name in file_names:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            raw_ts = os.path.getmtime(file_path)
            file_ts = datetime.fromtimestamp(raw_ts)
            raw_age = now - file_ts
            if raw_age.days > 3:
                stale = "** STALE **"
            else:
                stale = "FRESH"
            file_size = os.path.getsize(file_path)
            if file_size > 1000:
                print(f"   {file_size:8d} {file_name:40s} {stale}")
