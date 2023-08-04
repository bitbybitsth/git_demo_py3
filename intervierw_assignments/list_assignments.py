"""Write a function that accepts list as a input and returns the same list without duplicate elements, without using set"""



# def remove_duplicates_v1(dup_list):
#     unique = set(dup_list)
#     return list(unique)
#
# unique_list = remove_duplicates_v1([5,6,9,2,5,9,4,3,6,8,4,2,2,2,6,3,5,7,8])
# print(unique_list)


def remove_duplicates_v2(dup_list):
    unique = []
    for number in dup_list:
        if number not in unique:
            unique.append(number)

    return unique

# unique_list = remove_duplicates_v2([5,6,9,2,5,9,4,3,8,4,6,3,7,8])
# print(unique_list)

def remove_duplicates_v3(dup_list):

    for number in dup_list:
        num_count = dup_list.count(number)
        if num_count > 1:
            for i in range(num_count-1):
                dup_list.remove(number)
    return dup_list

unique_list = remove_duplicates_v3([5,6,9,2,5,9,4,8,4,4,4,4,4,6,3,7,8,5,5])
print(unique_list)


#############
# write a function that accepts a string of parenthesis as input and determine if string is of balanced paranethesis
# "{[(){([]({}))}]}"


def is_balanced(st):
    brackets = {"{": "}", "[": "]", "(": ")"}
    open_brackets = list(brackets.keys())
    close_brackets = list(brackets.values())
    stack = []
    for s in st:
        if s in open_brackets:
            stack.append(s)
        if s in close_brackets:
            s_open = open_brackets[close_brackets.index(s)]
            if len(stack) > 0:
                if s_open != stack.pop():
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

st = "{[{()}]}}"
check = is_balanced(st)

if check:
    print(f" {st}is balanced")
else:
    print(f" {st} is not balanced")




