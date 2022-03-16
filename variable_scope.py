
x = 100  # global variable -- visible to end of file

def spam():
    print("in spam(): x is", x)
    y = 50  #  local variable -- visible to end of function
    return y

result = spam()

print(x, result)

