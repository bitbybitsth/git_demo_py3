# inp_1 = 0
# inp_2 = 0
#
try:
    inp_1 = int(input("Enter one number"))
    inp_2 = int(input("Enter second number"))
    div = inp_1/inp_2
except Exception:
    print("One of the input is not and integer or float value")
#
# try:
#     inp_1 = int(input("Enter one number"))
#     inp_2 = int(input("Enter second number"))
#     div = inp_1/inp_2
# except ValueError:
#     print("One of the input is not and integer or float value")
# except ZeroDivisionError:
#     print("Second input cannot be zero")
#
#
# numbers = input("enter 10 comma separated number").split(",")
#
# i = 0
# sum = 0
# try:
#     while i<10:
#         sum = sum + int(numbers[i])
#         i +=1
# except IndexError:
#     pass
# except ValueError:
#     print("one of the number was incorrect, all valid number before the invalid number has"
#           "been added up and sum is displayed")
#
# print(sum)


# ZeroDivisionError
# ValueError
# IndexError
# TypeError
# print("hello"+10)
# KeyError
d = {1:2}
# try:
#     print(d[3])
# except KeyError:
#     print("key not present")
# print(d.get(3))
# FileNotFoundError
# try:
#     with open("wtc result.txt") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("no such file exists")

# try:
#     import std
# except ModuleNotFoundError:
#     pass

try:
    pass
except (ValueError, KeyError, IndexError, FileNotFoundError):
    pass
else:
    pass
finally:
    pass

