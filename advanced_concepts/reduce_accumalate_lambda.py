# reduce
from functools import reduce

import operator


def greater(a,b):
    return a if a>b else b
# def reduce_list(first, second):
#     return first.append(second)

result = reduce(operator.add, [45,67,87,45,67,34,56,22],10000)
print(result)

result = reduce(greater, [45,67,87,45,67,34,56,22])
print(result)


result = reduce(operator.mul, [45,10,45,23,56,23], 10)
print(result)

# input_str = input("Enter comma separated numbers")
# try:
#     num_list = [int(num) for num in input_str.split(",")]
# except ValueError:
#     num_list = []
#
# # result = reduce(, [3,4,5], 10)
# print(result)

# accumlate
from itertools import accumulate

num_list = [45,67,87,45,67,34,56,22]

result = list(accumulate(num_list, operator.add))
print(result)

#lambda functions
# lambda function are called anonymous functions, means they don't have any name
# lambda functions can take n number of inputs but can only execute one expression
# they are fast in processing
# best approach to use if we don't want define a function just execute some operation

num_list = list(range(1,101))

even_list = list(filter(lambda num: (num%2==0),num_list))
print(even_list)

greater = reduce(lambda a,b: a if a>b else b,[45,67,87,45,67,34,56,22])
print(greater)

map_result = list(map(lambda s: str.upper(s), ["text", "mon", "day"]))
print(map_result)
# for item in even_list:
#     print(item*2

cube = list(map(lambda y: y*y*y, [1,4,5,6]))
print(cube)


# d = {400:202, 100:404, 500:606}
# print(d.items())
# dictionary_filter = sorted(d.items(), key=lambda x: x[1],reverse=True)
# print(dictionary_filter)
# wapas_dict = {key:val for key, val in dictionary_filter}
# print(wapas_dict)

import collections

dup_list = [45,56,76,45,67,78,99,99,99,33,44,55,44,55]
print(collections.Counter(dup_list))

d = {}
for num in dup_list:
    if num not in d:
        d[num] = dup_list.count(num)

print("items", d.items())
print(d)


sorted_dict = sorted(d.items(), key= lambda x:x[1], reverse=True)
print()
d = {key: val for key, val in sorted_dict}
print(d)

x = (45, 2)

tup_list = [(56, 1), (76, 1), (67, 1), (78, 1), (99, 3), (33, 1), (44, 2), (55, 2)]
tup_list.sort()
print(tup_list)

print((1,99,99)>(2,3,4))




