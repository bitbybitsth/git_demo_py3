# pallindrome

def is_pallindrome(s1):
    return s1 == s1[::-1]

# anagram - "silent" "listen"


def is_anagram(s1, s2):
    if len(s1) == len(s2):
        for s in s1:
            if s not in s2:
                return False
        return True
    return False


def check_anangram(s1, s2):
    return sorted(s1) == sorted(s2)
#
# print(is_anagram("listen", "silent "))
# print(check_anangram("listen", "silent "))
#
# print(sorted("listny"))
# print(sorted("silent"))

"""write a function that accepts a string and returns the vovel count and consonants count, present in the string"""

#--------------------------------------------------------------------------------------------------------------------
# string reverse

# using slicing

# print("akshay trithiya"[::-1])

# using loop
# y = "incorporate"
# rev_y = ""
# for i in y:
#     rev_y = i + rev_y
# print(rev_y)

# using recursion

z = "retro"

def string_reverse(s1):
    if len(s1) == 0:
        return s1
    else:
        return string_reverse(s1[1:]) + s1[0]

# print(string_reverse(z))

p = "inadequate"
# using stack

def using_stack(p):
    stack = []

    for chr in p:
        stack.append(chr)

    s = ""
    for _ in range(0, len(stack)):
        s += stack.pop()

    return s

print(using_stack(p))

## using reverse function

b = "propoganda"

print("".join(reversed(b)))

#---------------------------------------
# rotational string

# panpan  -> anpanp -> npanpa -> panpan -> anpanp-

x = input("enter first string")
y = input("enter second string")

if y in x+x:
    print("rotational")
else:
    print("non rotational")