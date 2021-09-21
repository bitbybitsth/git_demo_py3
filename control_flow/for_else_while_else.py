# print all prime numbers less than the given input.
import math
num = int(input("enter a number"))




# for num in range(2,number):
#     for i in range(2, int(math.sqrt(num))+1):  # [2,.....,15]
#         if num%i==0:
#             print(f"{num} -> not prime")
#             break
#     else:
#         print(f"{num} -> prime")

# Nested loop

# for i in range(1,11):
#     print("##")
#     for j in range(1, 11):
#         print(f"{i} * {j} = {j*i}")
#         if j%7==0:
#             break
#     print("**")

def is_prime(num):
    for i in range(2, num + 1):  # [2,.....,15]
        if num % i == 0:
            print(f"{num} -> is not a prime number")
            break
    else:
        print(f"{num} -> is a prime number")


num = int(input("ennter"))
is_prime(num)
# num = int(input("ennter"))
# is_prime(num)
# num = int(input("ennter"))
# is_prime(num)
# num = int(input("ennter"))
# is_prime(num)
# num = int(input("ennter"))
# is_prime(num)


