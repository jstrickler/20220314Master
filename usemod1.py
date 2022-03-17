import sys
#  from pkg.pkg import module
#  NOT from pkg/pkg import module
from johnapp.math import geometry

a1 = geometry.circle_area(22)
print("a1: {}".format(a1))

a2 = geometry.rectangle_area(10, 37)
print("a2: {}".format(a2))

# module search locations
# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (where Python is installed)  (sys.prefix/lib)

for path in sys.path:
    print(path)
print()

print(sys.prefix)
