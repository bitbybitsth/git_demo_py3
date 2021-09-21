# # zip
# days = ["mon", "tue", "wed", "tHu", "fri", "sat", "sun"]
# day_in_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
#
# # i = 0
# # while i<len(days):
# #     print(f"{days[i]}  -> {day_in_num[i]}")
# #     i+=1
#
# # for index, num in enumerate(day_in_num):
# #     print(f"{days[index]}  -> {num}")
#
#
# zip_list = zip(days,day_in_num, month)
# print(zip_list)
#
# s = (("mon", 1,"jan"), ("tue", 2, "feb"), ("wed", 3, "mar"))
# #
# # for day, num, month in zip_list:
# #     print(f"{day}  -> {num} - > {month}")
#
# # zip longest
# # -----------------------
# from itertools import zip_longest
#
# zip_longest = zip_longest(days, day_in_num, month,fillvalue="*")
#
# # for day, num, month in zip_longest:
# #     print(f"{day}  -> {num} - > {month}")
#
# # filter
#
# num_list = list(range(1,1000))
# # write a program that will print a list of even numbers between 1 and 1000
#
# even_list = [num for num in num_list if num%2==0]
# print(even_list)
#
# # write a program that will print a list of prime numbers between 1 and 1000
# def is_prime(n):
#     if n==2:
#         return True
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return True
#     else:
#         return True
#
# # prime_list = []
# # # for num in num_list:
# # #     prime = is_prime(num)
# # #     if prime:
# # #         prime_list.append(num)
# # #
# # # print(prime_list)
# #
# # prime_list = list(filter(is_prime, num_list))
# # print(prime_list)
# #
# # title_days = list(filter(str.islower, days))
# # print(title_days)
# #
# # print("teXt".islower())
#
#
# # map
# names = ["sachin tendulkar", "brian lara", "ricky ponting", "muthaiya murlidharan", "glenn mcGrath", "jack kaLLis"]
# capitalized_names = list(map(str.title, names))
# print(capitalized_names)
#
# # Glenn McGrath
#
# def capitalised_names(name):
#     names = name.split(" ")
#     x = []
#     for nam in names:
#         nam = nam[0].upper() + nam[1:]
#         x.append(nam)
#     return " ".join(x)
#
# cutom_capitalised_names = list(map(capitalised_names, names))
# print(cutom_capitalised_names)
#
areas = [35.541546,56.686577,45.9782789,347.345435, 546546.4654646]
print(round(45.9782789))

#
# dec = list(range(1, len(areas)+1))
dec = [2]*len(areas)
print(dec)
round_areas = list(map(round, areas, dec))
print(round_areas)

