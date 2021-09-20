#from functions_intro import is_even
# Break and continue is used in loops
# pass can be used in if, elif else, loops, functions, class


# print(is_even(5))

#break - breaks the current loop whenever executed

#break
# for i in range(1,10):  # [1,2,3,4,5,6,7,8,9]
#     print("num", i)
#     if i%5==0:
#         break
#     print("square", i ** 2)


# Continue
# for i in range(1,1000):
#     print(i)
#     if i<50 or (i>100 and i<150):
#         continue
#     print("square", i ** 2)


for i in range(1, 15):  # [1,...14]
    print("num", i)
    if i % 3 == 0:
        continue
    if i % 9 == 0:
        break
    print("square", i**2)

if True:
    pass


# if i<10:
#     {}
# else:
#     {}


for i in range(1,10):
    pass

def function():
    pass



