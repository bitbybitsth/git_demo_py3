import copy
#
#
original_nums = [1, 2, 3, 4, 5, (1,2), "hello"]
copied_nums = original_nums.copy()

# copied_nums[-1] = "hi"

# copied_nums.append(6)
# print("original", original_nums)
# print("Copied", copied_nums)
#
users = [{"username": "vishal"}, {"username": "komal"}, [1,2,3,[{1:2, 4:[5]}]]]
copied_user = users.copy()
copied_users = copy.copy(users)

class Emp:

    def __init__(self,a):
        self.a = a

    def __str__(self):
        return f"{self.__dict__}"

e1 = Emp([10,20])

e2 = copy.copy(e1)
# print(e1)
# print(e2)


e2.a.append(30)
e2.b = 10





# print(e1)
# print(e2)
#
# copied_user[-1][-1][0][4].append(6)
# print("original user", users)
# print("copied users", copied_user)
#
# #
# # copied_user[0].update({"password":"*****"})
# # copied_user[-1].append(4)
# # copied_user.append({"username":"swapnil"})
# # copied_user[-1].update({"password":"***"})
# #
# # print("original", users)
# # print("copied", copied_user)
# #
# # # shhallow copy: it only copies the outer object and just copies the references of the inner object
# #
# # a  = [[1,2], [3,4], [5,6]]
# # b = a.copy()
# #
# # # a.append([7,8])
# # b.append([9,10])
# #
# # print(a)
# # print(b)
#
# a[0].append("*")
# b[1].append("&")
#
# #
# #
# # print(a)
# # print(b)
#
#
# a  = [[1,2], [3,4], [5,6]]
# b = a.copy()
# # a = [<class list obejct at 43546544>,<class list obejct at 43546544>, <class list obejct at 43546544>]
# # b= [<class list obejct at 43546544>,<class list obejct at 43546544>, <class list obejct at 43546544>]
#
# b.append([9,10])
# # b= [<class list obejct at 43546544>,<class list obejct at 43546545>, <class list obejct at 43546546>,<class list obejct at 43546548>]
# a.append([7,8])
# # a = [<class list obejct at 43546544>,<class list obejct at 43546545>, <class list obejct at 43546546>, <class list obejct at 43546547>]
#
# a[0].append("*")
# b[1].append("&")
# b[0].append("#")
#
# temp = [1,2,"*"]
# btemp = [3,4,"&"]
#
# a.append([55,66])
# b.append([77,88])
#
# print(a)
# print(b)
#
# for item in a:
#     item.append("%")
#
#
# print(a)
# print(b)
# # shallow copy, it only creates a copy of outer object and copies the references of inner object.
# # so when we change a inner object we are chaing the object at a particular address hence it will reflected in both original and copied
#

# deepcopy


a = [[1,2], [3,4], [5,6]]
b = copy.copy(a)
# print(id(a))
# print(id(b))
# print(id(a[0]))
# print(id(b[0]))

c = copy.deepcopy(a)

a.append([7, 8])
c.append([9,10])

print(a)
print(c)

a[0].append("*")
c[1].append("&")

print(a)
print(c)


users = [{"username": "vishal"}, {"username": "komal"}, [1,2,3,[{1:2, 4:[5]}]]]
shallow_copy = users.copy()
copy_user = copy.deepcopy(users)

shallow_copy[-1][-1][0][4].append(6)
copy_user[-1][-1][0][4].append(8)

print(users)
print(shallow_copy)
print(copy_user)


# deep copy = not only creates a copy of orignal obejct but alos copies the inner objects recusively