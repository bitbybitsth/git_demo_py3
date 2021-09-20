# ternary operator
import math
print("condition is True") if 10 % 2 == 0 else print("Condition is False")

if 10%2==0:
    print("true")
else:
    print("False")

print("true") if 10%2==0 else print("false")

today = "monday"
hour = "am"
x = "9AM" if hour=="am" else "9PM"

print(x)

#list comprehension

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):  # [2,.....,15]
        if num % i == 0:
            return False
    else:
        return True

number_list = list(range(1,101))


# num_list = []
# for num in range(1,101):
#     if is_prime(num):
#         num_list.append(num)

num_list = [num for num in range(1,101)]
print(num_list)
odd_list = [item for item in range(1,101) if item%2 != 0]
print(odd_list)
prime_numbers = [item for item in number_list if is_prime(item)]
print(prime_numbers)

# prime_numbers = []
# for item in number_list:
#     if is_prime(item):
#         prime_numbers.append(item)

days = ["mon", "wed", "fri", "sun"]

string = "mon,fri,tue,thu,sat,pan,the,upe,mon"

valid_days = [day for day in string.split(",") if day in days]
print(valid_days)

# valid_days = []
# sampel_days= string.split(",")
# for day in sampel_days:
#     if day in days:
#         valid_days.append(day)


s = "abcdefghijklmnopqrstuvwxyz"
ascii_small = [ord(c) for c in s]
print(ascii_small)

# dictionary comprehension

char_dict = {item: chr(item) for item in range(0, 257) if item%2==0}

# char_dict ={}
# for item in range(0,257):
#     if item%20==0:
#         char_dict.update({item:chr(item)})


print(char_dict)
print(type(char_dict))

# set compregesion
s  = "abcdefghijklmnopqrstuvwxyz,asderw3eqwaddsvfrqwdsgf3qvqfavwefdxcvg3qw"
set1 = {item for item in s}
# set1.add()
print(set1)
print(len(set1))


