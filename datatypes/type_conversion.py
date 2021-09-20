# Converting value of one dataype to another datatype is called type conversion or type casting.

"""
There 2 type of type conversion in python.

•	Implicit Type Conversion
•	Explicit Type Conversion

"""

# Implicit Type Conversion:
# Python automatically converts one data type to another. We don’t need to involve here.
#
# Python avoids loss of data in implicit type conversion.

n1 = 5
n2 = 10.4

sum = n1+n2

print("tyoe of n1", type(n1))
print("tyoe of n2", type(n2))
print(sum)
print("type of sum", type(sum))


#
# Explicit Type Conversion:
# In this type conversion programmer converts the datatype of object from one to another, by using function like int (), float () str (), list (), tuple (), set ().
# This is also called type casting as programmer casts the dataype of objects.
#
# Data loss may happen as programmer enforces the conversion

# str()

s1 = str(3455342345324535)
print(s1)
print(type(s1))

print(str(4.55644))

sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

sizes_set = set(sizes)
sizes_tuple = tuple(sizes)
print(sizes_set)
print(sizes_tuple)

sizes_dict = dict.fromkeys(sizes, "bytes")
print(sizes_dict)

sizes_str = str(sizes)
print(sizes_str)
print(type(sizes_str))
print(sizes_str[0])

print(",".join([str(x) for x in sizes]))

print(int(15.4))

print(int("34"))

cricket_team = {
    "captain": "Virat",
    "coach": "ravi shastri",
    "vc": "rohit sharma",
    "wk": "Pant",
    "management": "BCCI",
    "bowlers": {"fast": ["bumrah", "bhuvi"], "spin": ["chahal", "kuldeep"]},
}

print(list(cricket_team))


l = [3,4,6,7,8,3,4,5,7,4,3,6,7,4,3,5,64,24,5,43,4,5,4]
s = set(l)
l = list(s)
print(l)
