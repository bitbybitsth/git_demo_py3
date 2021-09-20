
str1 = "hello"
str2 = 'GOOD'
month = "april"
str3 = """Today is is Tuesday, 
29th day of Month April.
covid situation is getting better considering the recent days.
"""

#--------------------------------------
# upper() = returns the uppercase string
upper = str1.upper()
print(str1)
print(upper)

#- lower() - return the lowercase string
lower = str2.lower()

print(lower)

# user_input = input("Enter a string")
# print(user_input)
#
# if user_input.lower() == month.lower():
#     print("correct month")

#----------------------------

# replace(<sub1>, <sub2>) - returns the string by replacing sub1 with sub2

print(str3.replace("29", "30"))
print(str3)

tounge_twister = "she sells she shells on the she shore"
print(tounge_twister.replace("she", "he",1))

#----------------------------
# split()  -  splits the string and returns the list of the sprlitted data, by default uses string to split the string

splitted = tounge_twister.split()
print(splitted)

# splitted2 = str3.split("29")
# print(splitted2)

file_path = "D:/3BP3/pycharm/datatypes/string_introduction.py"
file_path_split = file_path.split("/")
file_name = file_path.split('/')[-1]

file_ext = file_name.split('.')[-1]
print(file_ext)

#---------------------------------------------------------
# string reverse

print("reversed tounge twister string:",tounge_twister[::-1])
print(str1[::-1])

split = tounge_twister.split()
split.reverse()
print("reversed lkist", split)

#---------------------------------------------
# join(iterable) - used to join a list

reversed_sentence = " ".join(split)
print(reversed_sentence)

file_path = "D:/3BP3/pycharm/datatypes/string_introduction.py"
file_path_split = file_path.split("/")
print(file_path_split)
print("/".join(file_path_split))

#---------------------------------------------
# strip() - removes the starting and trailing spaces/tabs/newlines
#
# user_input = input("Enter a string:")
# print(user_input)
#
# stripped_str = user_input.strip()
# print(stripped_str)
#
# stripped_str_char = user_input.strip("*")
# print(stripped_str_char)
#
# #-----------
# # rstrip() - strips from right
# # lstrip() - strips from left
#
# r_strip = user_input.rstrip("*")
# l_strip = user_input.lstrip("*")
#
# print("Rigth strip:", r_strip)
# print("left strip:", l_strip)

#------------------------------------
# count -  return the count of teh substring

print(tounge_twister.count("she"))


#------------------------------------------
print(tounge_twister.capitalize())
print(tounge_twister.title())

#-------------------------------
# startwith("<substring>") - returns true is teh string startswith the sub string else false.
# endswith("<substriung>")

print(str3.startswith("Today"))
print(str3.endswith("Today"))

#-----------------------------
# find() returns the index of the first occurence of the sub string, returns -1 if subtring is not present

# tounge_twister = "she sells she shells on the she shore"
length = len(tounge_twister)

print(tounge_twister.find("she"))
print(tounge_twister.find("she", 8))
print(tounge_twister.find("she", 15, 26))



