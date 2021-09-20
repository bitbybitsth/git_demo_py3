"""
Functions are the block of organized code implemented to perform a single related action.
Functions can be reused whenever required.
Functions can accept parameter and return some value.
“return” keyword to return a value from function.

syntax:

def <function_name>(<optional parameter>,<optional parameter n>):
    code block
    code block
    return some value <optional>
"""


def test_func():
    num=10
    if num%2 != 0:
        print("odd")

# test_func()
# test_func()
# test_func()

def is_even(num):

    if num % 2 == 0:
        return True

    return False
#
# is_even(10)
#
# stat = is_even(11)
# print(stat)
# print(type(stat))
#
# if is_even(10):  # positional arguments
#     print("even")
#
# if not is_even(num=23): # keyword arguments
#     print("odd")
#
#
# print("Even", is_even(20))
# print("Even", is_even(21))


# write a function which checks whether a given string is pallindrome or not
# madam


def check_pallindrome(s1):
    if s1 == s1[::-1]:
        return True


if check_pallindrome("madam"):
    print("pallindrome")


if not check_pallindrome("test"):
    print("not a pallindrome")

stat = check_pallindrome("madam")
stat1 = check_pallindrome("monday")
print(stat)
print(stat1)

