# class Student:
#     def __init__(self, roll, name, sec):
#         self.roll = roll
#         self.name = name
#         self.section = sec
#
#
# s1 = Student(1,"akshay", "2nd")
# print(s1.name)
# print(s1.section)


class Car:
    def __init__(self):
        print("inside constructor")

    def test_sample(self, a, b, *args, d=10):
        pass


# c = Car()
# c1 = Car()

# class ObjectOrientedProgramming:


class Employee:

    organisation = "Bit by Bit STH"


#
#     def __init__(self, eid, name,):
#         self.employee_id = eid
#         self.full_name = name
#         # self.age = age
#         # self.work_email = email
#         # self.pay = salary
#         # self.gender = gender
#
#     def save_details(self, id, name):
#         self.employee_id = id
#         self.full_name = name
#
#     def display_detail(self):
#         print(self.employee_id)
#         print(self.full_name)
#         # print(self.work_email)
#         # print(self.pay)
#         # print(self.age)
#         # print(self.gender)
#
#     def raise_salary(self, raise_percentage):
#         # self.pay += 10*raise_percentage
#         pass
#
#     # def tes1(self):
#     #     pass
#     #
#     # def test10000(self):
#     #     pass
#
#
# # e1 = Employee(1, "salman", age=55, email="flop@radhe.com", salary=20000.0, gender="M")
e2 = Employee()
#
# # # e1.display_detail()
# # e1.raise_salary(0.10)
# # print(e1.pay)
#
# # e2.raise_salary(0.20)
# # print(e2.pay)
#
# e3 = Employee(3, "sunny")
# e3.display_detail()
# e3.raise_salary(3)
#
# e3.age =
class Emp(Employee):
    pass


d = Emp()
print(isinstance(e2, Emp))
print(isinstance(d, Employee))

print(issubclass(Emp, Employee))
