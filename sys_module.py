import sys

print("sys.argv: {}\n".format(sys.argv))

print("sys.path: {}\n".format(sys.path))

print("sys.prefix: {}\n".format(sys.prefix))

print("sys.executable: {}\n".format(sys.executable))

print("sys.version: {}\n".format(sys.version))

print("sys.version_info: {}\n".format(sys.version_info))

print("sys.version_info.major: {}\n".format(sys.version_info.major))

print("sys.platform: {}\n".format(sys.platform))

#  linux darwin win32

for name in dir(sys):
    if not name.startswith('_'):
        print(name)
print('-' * 60)

print(dir(sys))
print('-' * 60)
# sys.exit(1)  # success. Use sys.exit(1) for error

print("sys.maxsize: {:,d}\n".format(sys.maxsize))

# sys.stdout  sys.stderr  sys.stdin

print("I have a bad feeling about this", file=sys.stderr)






