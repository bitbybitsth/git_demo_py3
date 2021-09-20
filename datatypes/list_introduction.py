"""
List:
•	Backed by Array
•	Index Based - start from 0 - Index can be Positive and Negative - Positive Index >=0, Negative Index <=-(Length)
•	# E.g.: a [-2] is a[length-2]
•	Holds homogeneous + heterogeneous data elements (For Hetro Every element is treated as Object)
•	Mutable - can append/add/replace/remove/update
•	Sequence Order is Preserved
•	Duplicates are Allowed
•	Multiple None Type Allowed
•	Ideal for searching and retrieval
•	Insertion and Deletion are costly operations

inbuilt methods: append, insert, extend, copy, count, reverse, sort, pop, remove, clear, index
"""

# <name_for_list> = [<Elements seperated by comma>, <Elements seperated by comma>, <Elements seperated by comma>]
# <name_for_list> = list(<Elements seperated by comma>, <Elements seperated by comma>, <Elements seperated by comma>)
# empty_list = []
# empty_list = list()


#--------------------------------------------------------------------

# defining the list
list_of_denominations = [1, 5, 10, 50, 100, 500, 20, 1000, 2]
# list_of_denominations = list(1, 2, 5, 10, 20, 50, 100, 500, 1000)
print("list of denominations", list_of_denominations)

#--------------------------------------------------------------------
length_of_list = len(list_of_denominations)
print("length of denimiations list is :", length_of_list)

#--------------------------------------------------------------------

# append - Appends an element at the end of the list

list_of_denominations.append(2000)
print("list of denominations after appending 2000", list_of_denominations)

#--------------------------------------------------------------------
# insert - syntax - insert(<index>, <element>), inserts the elements at give in index

list_of_denominations.insert(7, 200)
print("after inserting 200", list_of_denominations)

#--------------------------------------------------------------------

# extend  - extends te current list with list provided in function

didgital_curreny = ["gpay", "pahonepay", "paytm"]

# list_of_denominations.extend(didgital_curreny)
# print("after extending th list with new cuurency", list_of_denominations)

# x +=10
# x = x+10

list_of_denominations += didgital_curreny
print("after extending th list with new cuurency", list_of_denominations)

#--------------------------------------------------------------------

# count = returns the count of an given element present inside the list

count = list_of_denominations.count(200)
print("count of 200", count)
#--------------------------------------------------------------------
# reverse - reverses the list

# list_of_denominations.reverse()
# print("reversed list", list_of_denominations)

#--------------------------------------------------------------------
# index  - retunr the index of the given element

index_of_500 = list_of_denominations.index(500)
print("index of 500", index_of_500)

#--------------------------------------------------------------------
# pop - removes the last elememt of the list

last_element = list_of_denominations.pop()
# print(list_of_denominations)
list_of_denominations.pop()
# print(list_of_denominations)
list_of_denominations.pop()
print("last element", last_element)
print("after popping 3 elemnts", list_of_denominations)

#--------------------------------------------------------------------

# remove - removes the given element from the list

list_of_denominations.remove(1000)
print("after remove", list_of_denominations)


#--------------------------------------------------------------------
# copy  - return a copy of the list

copied_list = list_of_denominations.copy()
copied_list.insert(0, "50ps")
print("copied list", copied_list)
print("original list", list_of_denominations)

#--------------------------------------------------------------------
# sort - sorts the list

list_of_denominations.reverse()
print("reversed", list_of_denominations)

list_of_denominations.sort()
print("sorted list", list_of_denominations)

list_of_denominations.sort(reverse=True)
print("Descending list", list_of_denominations)


# clear - clears the list

list_of_denominations.clear()

print("cleared list", list_of_denominations)

list_of_denominations.append(1)
print(list_of_denominations)
# ----------------------------------------

reding = [56,78,234,7753,7753, 7753,"fgf"]

print(reding[3])
print(reding[-1])












