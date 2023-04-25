def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
bad_fun(0)
print()

def bad_fun(n):
    return 1 / n
try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
print()

def bad_fun(n):
    prin("this is function")
    return 1 / n
try:
    bad_fun(0)
except (ArithmeticError, NameError):
    print("2 error!")
