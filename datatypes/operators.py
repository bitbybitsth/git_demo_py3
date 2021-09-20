

# Logical

# if not x%2==0:
#     print("You are correct")
#     print("if scope")
# else:
#     print("you are wrong")
#     print("else scope")

list_of_numbers = [45,67,89,23,523,45,23]
sum = 0

for item in list_of_numbers:
    sum += item



# print("Total", sum)
#
# d = {45:"forty five", 68:"sixty seven"}
#
# if 68 not in list_of_numbers:
#     print("67 absent")


list_of_new_numbers = list_of_numbers

print(list_of_new_numbers is list_of_numbers)
print(list_of_new_numbers is not list_of_numbers)

x=444
y=444
print(y is x)