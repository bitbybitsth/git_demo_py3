# Nested function
#
#
# def outer():
#     print("from outer")
#     def inner():
#         print("from inner")
#         print("exiting innner")
#     inner()
#     print("exiting outer")
#
# outer()

# recursive function - a function that calls itself is a recrusive function

def fun():
    fun()

# fun()
#
# 5 = 5*4*3*2*1
# 5 = 1*2*3*4*5

# def factioral(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact *i
#     return fact
#
# print(factioral(5))


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

fact = factorial(5)
print(fact)


