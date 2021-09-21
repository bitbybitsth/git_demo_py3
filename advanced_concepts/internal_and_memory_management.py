# x = 10
#
# x = x - 10
# x = x/0
#
# print(x)

num = 10
# tenth = num
# dus = 10
# tenth = "tenth"
#
# print(id(num))
# print(num)
# print(tenth)
# print(id(tenth))
# # ------------
# num = num+1
# print(id(num))
# print(tenth)
# tenth = tenth +2
# tenth = 55
# tenth = "tenth"

def function():

    first = 0
    scond = 1
    print(first, scond)
    for i in range(2,num):
        third = first + second
        print(third)
        first, second = second, third
        if i >3:
            return
        function()

# function()

x = 10
y = x

y = y + 2

# print(id(x) == id(y))
#
# print(x is y)

# ------------
print("integers")
print(id(x) == id(y))

print("string")
x = "hello"
y = "hello"
print(id(x) == id(y))


print("list")
x = [1]
y = [1]
print(id(x) == id(y))

print("dictionary")
x = {1:2}
y = x
print(id(x) == id(y))

# y.popitem()
# y.update({3:4})

print("tuples")
x = (1)
y = (1)
print(id(x) == id(y))
x = (2)
y = (3)

