"""
Sets:

•	Backed by Hash table - Open address a.k.a closed hashing
•	No Index Based Operations Allowed
•	Holds homogeneous + hetrogeneous data elements (For Hetro Every element is treated as Object)
•	sets are Mutable - can add/remove/update
•	but the elements of set should be immutable
•	Sequence Order is Not Preserved
•	Duplicates are not Allowed
•	Single None Type Allowed


•	Ideal for Insertion and Deletion
•	Searching and retrieval might be costly operations
•

Set methods: add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset,
pop, remove, symmetric_difference, symmetric_difference_update, unioun, update.


How to use/Declare:

new_set = {immutablelement1, immutablelement2, immutablelement3}
new_set = set ([ immutablelement1, immutablelement2, immutablelement3])
empty_set = set()
eg:
set1 = {1, 3, 2, 4, 8, 9, 0}
set2 = set ([1, 3, 7, 5, 4, 0, 7, 5])

"""

set1 = {1,2,3,4,5,6}
set2 = set([5,6,7,8,9,10])

print("set1: ", set1)
print("set2: ", set2)

#---------------------------------
# union - returns the unioun of the set

union_set = set1.union(set2)
print(union_set)

#---------------------------------
# intersection() - returns the intersection of the sets

intersection_set = set1.intersection(set2)
print(intersection_set)

# set1.intersection_update(set2)
# print("intersection update", set1)


#---------------------------------
# difference  - returns the difference of the sets

a_minus_b = set1.difference(set2)
print("A-B", a_minus_b)

b_minus_a = set2.difference(set1)
print("B-A:", b_minus_a)

# set2.difference_update(set1)
# print("difference update", set2)
#
# #---------------------------------
# # symmetric difference - returns the symmetric difference of the set

symm_diff = set1.symmetric_difference(set2)
print("Symmetric difference", symm_diff)

# set1.symmetric_difference_update(set2)
# print("symm diff update", set1)

# #---------------------------------
# issubset - returns True or False if calling set is a subset of passed set

print("is subset", set1.issubset({1,2,3,4,5,6,7,8}))
print("is subset", set1.issubset(set2))

#---------------------------------
# issuperset - return True if calling set is a superset of passed set else False

print("is super set", set2.issuperset({7,8,9}))
print("is super ser", set2.issuperset(set1))

#---------------------------------
# isdisjoint -  returns true is the sets are disjoint else false

print("disjoint", set1.isdisjoint(set2))
print("is disjoint", set1.isdisjoint({7,8,9}))

#---------------------------------
# add(<element>) - adds the element to teh set

set1.add(4)
print("after adding 4", set1)


set1.add(7)
print("after adding 7", set1)

#---------------------------------
# pop() removes an random element from the set and returns it
element = set1.pop()
print(element)
print(set1)

#---------------------------------
# remove(<element>) - removes the element from the set if present else throws and keyerror

set2.remove(9)
print(set2)
# set2.remove(11)
# print(set2)
#---------------------------------
# discard(<element>) - removes  the element from the set if present else does not throw any error

set1.discard(11)
print(set1)

#---------------------------------------------------------
# update(<Set>) - updated the calling set with passed set


set1.update({1,2,3,4,5,6,7,8,9})
print(set1)

#---------------------------------------------------------
# copy() - returns the shallow copy of the set

set3 = set1.copy()

#---------------------------------------------------------
# clear() - clears the set

set1.clear()
set2.clear()
print(set1)
print(set2)


















