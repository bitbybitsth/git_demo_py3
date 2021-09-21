class MultipliedByZero(Exception):
    pass

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    if a==0 or b==0:
        raise MultipliedByZero
    return a*b

def div(a,b):
    if b==0:
        raise ZeroDivisionError("second argument cannot be zero")
    return a/b

def mod(a,b):
    return a%b
