"""
Tuple

•	Very Similar to lists
•	Index Based Operations Allowed
•	Holds homogeneous + hetrogeneous data elements (For Hetro Every element is treated as Object)
•	Immutable Cannot be Changed
•	Sequence Order is Preserved
•	Duplicates are Allowed
•	Multiple None Type Allowed

inbuilt methods: count, index

"""

# tuple intro

# defining tuple
# <name_for_tuple> = ("<elements seperated by comma>", "<elements seperated by comma>", "<elements seperated by comma>")
# <name_for_tuple> = tuple(["<elements seperated by comma>", "<elements seperated by comma>", "<elements seperated by comma>"])
# empty_tuple = ()
# empty_tuple = tuple()


months = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")
days_of_week = tuple(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])

# months_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# months_list.remove("JAN")


print(months)
print(days_of_week)


print(months[0])
print(months[-1])

count = months.count("JAN")
print("jan", count)

print("DEC count", months.count("DEC"))

index = days_of_week.index("tue")
print("tuesday ", index)


# x = [1,2,3]
#
# print(x.sort(reverse=True))
# print(x)

# print(months[4:5])






