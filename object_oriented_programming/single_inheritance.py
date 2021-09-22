class Employee:

    organisation = "Bit By Bit"
    address = "Pune"
    basic_hike = 0.10

    def __init__(self, eid, name, email, contact, age, gender, address, salary=20000):
        self.eid = eid
        self.name = name
        self.email = email
        self.contact = contact
        self.age = age
        self.gender = gender
        self.address = address
        self.salary = salary
        # self.all_personal_details = [{"key": "value"}]

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


# e1 = Employee()
class Developer(Employee):
    def __init__(
        self, eid, name, email, contact, age, gender, address, salary, skill, task
    ):
        super().__init__(eid, name, email, contact, age, gender, address, salary)
        self.skill = skill
        self.task = task

    def begin_web_development(self):
        pass

    def raise_pull_request(self):
        pass

    def give_demos(self):
        pass

    def deploy_website(self):
        pass


d1 = Developer(
    1,
    "rahul",
    "rahul@bitbybitsth.com",
    674579587,
    23,
    "m",
    "Pune",
    500000,
    "python",
    "design & development",
)
d1.apply_leave(2)
d1.appraisals()
print(d1.salary)
d1.begin_web_development()


class Tester(Employee):
    def __init__(
        self, eid, name, email, contact, age, gender, address, salary, skill, task
    ):
        super().__init__(eid, name, email, contact, age, gender, address, salary)
        self.skill = skill
        self.task = task

    def begin_web_development(self):
        pass

    def raise_pull_request(self):
        pass

    def give_demos(self):
        pass

    def deploy_website(self):
        pass


# def is_23_prime(num):
#     for i in range(2, num//2+1):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("Prime")
# def is_45_prime(num):
#     for i in range(2, num//2+1):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("Prime")
#
# def is_56_prime(num):
#     for i in range(2, num//2+1):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("Prime")

# def is_prime(num):
#     for i in range(2, num//2+1):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("Prime")
#
# is_prime(23)
# is_prime(45)
# is_prime(56)
# is_56_prime()
# is_45_prime()
# is_23_prime()
