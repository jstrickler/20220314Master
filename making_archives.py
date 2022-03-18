import shutil

shutil.make_archive('data', 'zip', 'DATA')
shutil.make_archive('data', 'tar', 'DATA')
shutil.make_archive('data', 'gztar', 'DATA')
shutil.make_archive('data', 'bztar', 'DATA')
