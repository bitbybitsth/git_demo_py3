
"""
for loop
while loop
expanded for loop
for else loop
while else loop
"""
denominations = [1, 5, 10, 50, 100, 500, 20, 1000, 2]

set1 = {1,2,3,4,5,6}

cricket_team = {
    "captain": "Virat",
    "coach": "ravi shastri",
    "vc": "rohit sharma",
    "wk": "Pant",
    "management": "BCCI",
    "bowlers": {"fast": ["bumrah", "bhuvi"], "spin": ["chahal", "kuldeep"]},
}


months = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")

tounge_twister = "she sells she shells on the she shore"
#------------------------------------------------------------------------------

# for loop

# on list
# print(denominations)
# for item in denominations:
#     print(item)
#     if item==50:
#         print("50 curreny is present")


# on tuple
m_start = []
# for month in months:
#     lower_month = month.lower()
#     print(lower_month)
#     if month.startswith("M"):
#         m_start.append(month)
#
# print(m_start)


# on set
# for element in set1:
#     print(element)

#
# # on string
# tounge_twister = "She Sells Sea Shells On The Sea Shore"
# space_count = 0
# caps_letters = []
# for letter in tounge_twister:
#     print(letter)
#     if letter.isupper():
#         caps_letters.append(letter)
#     if letter.isspace():
#         space_count +=1
#
#
# # print(tounge_twister.count(" "))
# print(caps_letters)
# print(space_count)

# On dictioanry
# cricket_team = {
#     "captain": "Virat",
#     "coach": "ravi shastri",
#     "vc": "rohit sharma",
#     "wk": "Pant",
#     "management": "BCCI",
#     "bowlers": {"fast": ["bumrah", "bhuvi"], "spin": ["chahal", "kuldeep"]},
# }

# for item in cricket_team:
# #     print(item)
#
# for key in cricket_team.keys():
#     print(key)
#
#
# for value in cricket_team.values():
#     print(value)

# for item in cricket_team.items():
#     print(item)
#     # print(item[0])
#
# # expanded for loop
# print(cricket_team.items())
# for key, value in cricket_team.items():
#     print(f"{value} is at position of {key}")

#-------------------------
# for loop with range

# # range(start,stop,step)
#
# range_list = list(range(1,1000,1))
# print(range_list)
# print(type(range_list))
# range_list.append(1000)
# print(range_list)


#
# for item in range(-1, -30, -1):
#     print(item)

#-----------------------------------------------------

# while loop


# while True:
#     x = int(input("enter a number:"))
#     if x%2==0:
#         break


#
# num = 0
# sum = 0
# while num<500:
#
#     num = int(input("Enter  a num"))
#     sum += num

    # sum = sum + num1
#
# # print(sum)
#
# num = int(input("Enter a num"))
# i = 0
#
# while i<num:
#     print("****")
#     i+=1
    # code
    # code
    # code

#------------------------------------
















