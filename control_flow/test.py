# def func(n):
#     looping = False
#     while not looping:
#         try:
#             item = iter(n)
#             looping = True
#         except StopIteration:
#             looping = True
#     for i in n:
#         print(i, end=" ")
# n = {4,7,0,3}
# print(func(n))
#
# def dec(func):
#     def prg(*args, **kwargs):
#         value = func(*args, **kwargs)
#         return value
#     return prg
#
# @dec
# def test(x,y):
#     return x+y
# x,y = 5,2
# print(test(x,y))

#
# def fun1(nums):
#     for num in nums:
#         if num%2==0:
#             yield num
#
# def func2(nums):
#     for num in nums:
#         yield num * 3
#
# def fun3(nums):
#     for num in nums:
#         yield num
#
# nums = [0,-1,-4,-9,-16,-25,-36,-49]
#
# res = fun3(func2(fun1(nums)))
# for num in res:
#     print(num, end=" ")
# #
# #
# # print(tuple("python"))
# from collections import Counter
# def fun(s1,s2):
#     c1 = Counter(s1)
#     c2 = Counter(s2)
#     d = c1 & c2
#     if len(d) == 0:
#         return 0
#     ch = list(d.elements())
#     c = sorted(ch)
#     return "".join(c)
# s1 = "python"
# # s2 = "hacerEarth"
# #
# #
# #
# # print(fun(s1,s2)
# # print("Bob""20", sep=",")
#
#
# def main_prog(f):
#     m = {}
#     def inprog(num):
#         if num not in m:
#             m[num] = f(num)
#         return m[num]
#     return inprog
#
# @main_prog
# def fun(num):
#     if num == 0:
#         return 1
#     else:
#         return num**2*fun(num-1)
# print(fun(3))

def fun(a):
    for i in a:
        if i not in b:
            b.append(i)
            a.remove(i)
    print(b)

a = [1,1,2,2,3,4,4,3,0,0]
b = []
fun(a)

print(a==b)
