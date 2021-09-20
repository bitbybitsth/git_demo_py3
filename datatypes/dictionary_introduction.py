"""
Dictionary:

•	internally implemented as hash table and uses closed hashing  a.k.a open addressing
•	Unlike other data types Dictionary holds a pair (KEY, VALUE) as a single element.
•	Dictionary is mutable
•	Key must be immutable (String, Number, Tuple) and no duplicates allowed.
•	Value can be of any type (Mutable or immutable) and duplicated are allowed.
•	elements are accessed using keys
•	can be nested
•	dictionary is unordered collection
•	insertion deletion is efficient and searching is not efficient compared to insertion/deletion.

Dict_methods:
copy (), clear (), fromkeys (), get (), items (), keys (), values (), pop (), popitem(), setdefault(), update()

how to use/create:
•	new_dict = {}
•	new_dict= newDict = {key1:value1, key2:value2, key3:value3, ...., key_n: value_n}
•	newDict = dict () / This will create a blank dictionary.
•	newDict = dict ({key1:value1, key2:value2, key3:value3, ...., key_n: value_n})
"""
# cricket_team = ["virat", "ravi shastri", "rohit sharma", "jasprit bumrah", "BCCI"]

cricket_team = {
    "captain": "Virat",
    "coach": "ravi shastri",
    "vc": "rohit sharma",
    "wk": "Pant",
    "management": "BCCI",
    "bowlers": {"fast": ["bumrah", "bhuvi"], "spin": ["chahal", "kuldeep"]},
}

#----------------------------------------------------------
# Accesing elements of dictioanry

print(cricket_team["wk"])
print(cricket_team["bowlers"]["fast"][-1])
print(cricket_team["management"])


#----------------------------------------------------------
# keys() - returns the list of keys

keys = cricket_team.keys()

print("keys of dictionary", keys)

#----------------------------------------------------------
# values() - returns the list of values

values = cricket_team.values()
print("values of dict", values)

#----------------------------------------------------------
# items() - returns the items of the dictionary

print("items of dict:", cricket_team.items())

#----------------------------------------------------------
# get() - return the value from the dictionary of the specified key, if the keys exists else returns None or the default value provided


print("Captain using get:", cricket_team.get("captain"))
print("captain using direct access:", cricket_team["captain"])

print("Physio using get:", cricket_team.get("physio"))
# print("Physio using direct access:", cricket_team["physio"])


#----------------------------------------------------------
# update() - takes a dictioanry as an argument and update the calling dictionary

cricket_team.update({"12th man": "vijay", "bench": ["natrajan", "prthvi shaw"]})
cricket_team.update()

print("updated dictionary", cricket_team)


#----------------------------------------------------------
# setdefault() - return the value of the key if the key is present
#                 if key not present creates the key in the dictionary with value as None
#                     if default value provided sets the key with the given default value

print("Vice captain", cricket_team.setdefault("vc"))

cricket_team.setdefault("umpires", "vk shamra")
print(cricket_team)


#----------------------------------------------------------
# popitem() - remove an random item from the dictionary

cricket_team.popitem()
print("after popitem 1", cricket_team)
cricket_team.popitem()
print("after popitem 1",cricket_team)
cricket_team.popitem()
print("after popitem 1", cricket_team)

#----------------------------------------------------------
# pop() - takes keys as argument/parameter and pops that key value pair

cricket_team.pop("vc")
print("after removing vc", cricket_team)
indian_team_coach = cricket_team.pop("coach")
print(indian_team_coach)


#----------------------------------------------------------
# copy() returns a shallow copy of dictionary


copied_dict = cricket_team.copy()

print("copied before pop", copied_dict)
copied_dict.popitem()

print("copy:", copied_dict)
print("original", cricket_team)

#----------------------------------------------------------
# clear() - clear the dictionary

cricket_team.clear()
print(cricket_team)

#----------------------------------------------------------
# fromkeys() - takes a list argument and creates the dictionary with elements of the list as dctionary keys with default value fro keys as None
#                 and if default value is provided then default values of key would be the provided default value


women_cricket_team_list = ["captain", "vc", "coach", "wk", "bowelers"]


women_cricket_team_dict = dict.fromkeys(women_cricket_team_list, "default")

print("women cricket team", women_cricket_team_dict)

women_cricket_team_dict["captain"] = "jhulan goswami"

print(women_cricket_team_dict)

women_cricket_team_dict["physio"] = "value"







