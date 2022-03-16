
# int float

i1 = 12345
i2 = 2930293582305982305982305928350928350928530298502935820958209582095802958029580293850298350
i3 = -333
print(i2 + i3)

i4 = 0x100
i5 = 0b100
i6 = 0o100
print(i4, i5, i6, '\n')

f1 = 123.4
f2 = .45235
f3 = 99.
f4 = 0.0

a = 23
b = 5

print(a + b, a - b)
print(a * b, a / b, a // b, a // -b, 23.0 // 5)
print(a ** b, a % b)

b += 5  # b = b + 5
b *= 6
b /= 4
print(b)

c = 10
d = 20

print(a * b + c / d)
# P E M/D A/S
print((a * b) + (c / d))
print(a * (b + c) / d)
print()

a = "123"
b = 456

print(int(a) + b)
print(a + str(b))

#  OK:   "123"   "    123"    "   123.323    "
# INVALID "123m"   "abc123"   "#123"  etc etc











