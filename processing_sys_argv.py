import sys

print("sys.argv: {}\n".format(sys.argv))

value = sys.argv[1]
print("value: {}\n".format(value))


for file_name in sys.argv[2:]:
    print("processing", file_name)
