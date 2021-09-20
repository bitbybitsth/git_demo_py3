
num_list = [5, 7, 8, 9, 3, 55, 77, 88, 33, 55, 22, 55, 77, 44, 22]


num_max = max(num_list)
num_min = min(num_list)
print(num_max)
print(num_min)

# eval(<expression>)

#
# print(dir(num_list))
#
# help(False)

quo, rem = divmod(55, 34)
result = divmod(55, 34)
print(quo)
print(rem)
print(result)

set1 = frozenset(num_list)

print(set1)

# range - range(start, stop, step) - returns a range object

# r_list = list(range(5,50,5))
# for i in range(2, 10):
#     print(i)

print(abs(-6))

#
# print(bin(31))
#
# d = bool(eval_res)
# e = bool(num_list)
#
# print(d)
# print(e)
#
#
# print(chr(69))
# print(chr(97))
#
# print(ord("^"))
# print(ord("p"))

# eneumerate()
# for item in num_list:
#     print(f"{item} is at index")
#
# for pos, element in enumerate(num_list, 0):
#     print(f"{element} is at {pos} position")

# format
expr = "5*4+66-54/2"
eval_res = eval(expr)

str1 = "{} is the result of {}".format(eval_res, expr)
print(str1)

str2 = f"{eval_res} is the result of {expr}"
print(str2)

print(hash("p"))

print(id(num_list))

print(oct(8))
print(hex(15))

print(pow(5,6))


print(55/3)
print(round(55/3))

sorted_list = sorted(num_list)
print(sum(num_list))



print(type(eval_res))

rev = list(reversed(num_list))
print(rev)
num_list.reverse()

students = ["student1", "student2", "student3"]
stu_di = {"prkash": 1, "rohit":2}


for rank, student in enumerate(students, 1):
    print(f"{student} is at {rank} position")


file_status_dic = {"xyz.txt": "success attached", "abc.png": "failed"}

file_status = ["xyz.txt:sucess", "abc.png:failed"]

for pos, item in enumerate(file_status, 1):
    print(f"{pos}-{item}")







