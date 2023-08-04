from datetime import datetime

# Variable types
# instance variable
# class variable

# Method types
# instance_method
# class method
# static method
a = 10


class Employee:

    organisation = "Bit By Bit"
    address = "Pune"
    basic_hike = 0.10

    def __init__(self, eid, name, email, contact, age, gender, address, salary):
        self.eid = eid
        self.name = name
        self.email = email
        self.contact = contact
        self.age = age
        self.gender = gender
        self.address = address
        self.salary = salary
        self.all_personal_details = [{"key": "value"}]

    def appraisals(self):
        self.salary += self.salary * Employee.basic_hike

    # def appraisals2(self):
    #     self.salary += self.salary * self.basic_hike

    def apply_leave(self, no_days):
        print(f"leave granted for {no_days}")

    @classmethod
    def announce_wfh(cls, no_of_months):
        print(f"wfh for {no_of_months}")

    @classmethod
    def rollout_payroll(cls):
        print("salary paid")

    @staticmethod
    def static_demo(a, b, c):
        pass

    def sample_instance_method(self):
        pass

    @classmethod
    def sample_class_method(cls):
        pass

    @staticmethod
    def date_formatting(now):
        format = "%Y-%m-%d %H:%M:%S"
        return now.strftime(format)


# e1 = Employee(1,"test", "test@doamin.com", 674579587,23,"m", "Pune", 500000)
# e2 = Employee(1,"test", "test@doamin.com", 674579587,23,"m", "Pune", 500000)
# # e1.appraisals()
# # print(e1.salary)
#
# # e2.appraisals()
# # print(e2.salary)
# # e2.basic_hike = .20
# # e2.appraisals2()
# # print(e2.salary)
#
# e1.apply_leave(2)
# e2.apply_leave(3)
#
# Employee.announce_wfh(3)
# e1.announce_wfh(2)
# e1.announce_wfh(4)
#
# Employee.apply_leave(e1, 4)
# e1.apply_leave(4)
#
# Employee.static_demo(10,20,30)
#
# print(type(e1))
# now = datetime.now()
# str_date = e1.date_formatting(now)
# print(str_date)
# print(type(str_date))
#
#
# now = datetime(2020,4,5)
# str_date = Employee.date_formatting(now)
# print(str_date)
# print(type(str_date))
#
# data = [{"key":"value"}]
