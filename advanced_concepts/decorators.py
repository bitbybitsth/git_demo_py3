
def outer(func):
    def inner(*args, **kwargs):
        print("_____________________________")
        func(*args, **kwargs)
        print("_____________________________")
    return inner

@outer
def test_decorator():
    print("This is to demonstarte decorators")

@outer
def test_decorator1():
    print("demonstartion 2")

# test_decorator()
# test_decorator1()


import time
from functools import wraps


def timer(func):

    @wraps(func)
    def inner(*args, **kwargs):
        """test wraps inner"""
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"Execution took total {t2-t1} seconds")
    return inner

# timer(fibonacci_series)

@timer
def fibonacci_series(n):
    """
    this is fibonacci series implementation
    :param n: total of numbers of the fibonacci series
    :return: None
    """
    first = 0
    second = 1
    print(0)
    print(1)
    for _ in range(2, n):
        third = first+second
        print(third)
        # first = second
        # second = third
        first, second = second, third

@timer
def is_balanced(st):
    brackets = {"{": "}", "[": "]", "(": ")"}
    open_brackets = list(brackets.keys())
    close_brackets = list(brackets.values())
    stack = []
    for s in st:
        if s in open_brackets:
            stack.append(s)
        if s in close_brackets:
            s_open = open_brackets[close_brackets.index(s)]
            if len(stack) > 0:
                if s_open != stack.pop():
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

is_balanced("(){}{}{}}}{{[[]]")
fibonacci_series(1000)

f = fibonacci_series
print(f.__doc__)

