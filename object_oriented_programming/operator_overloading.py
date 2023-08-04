from crud_operations_medicine import Medicine
from datetime import datetime

# print(10+20)
# print("hello"+"hi")
# print(5.5+4.5)


crocin = Medicine(
    1, "crocin", 10, datetime(2022, 1, 1), datetime(2019, 1, 1), "cipla", 20
)

crocin2 = Medicine(
    2, "disprin", 15, datetime(2021, 5, 10), datetime(2019, 1, 1), "mankind", 5
)

crocin + crocin2

# print(crocin.qty)


class Cart:
    def __init__(self, user, *products):
        self.user = user
        self.products = products

    def __len__(self):
        return len(self.products)


# u = Cart("user1", "mobile", "cover", "cleaner", "headphones")
# print(len(u))


class Student:
    def __init__(self, roll_no, phy=None, chem=None, math=None, bio=None):
        self.roll_no = roll_no
        if phy:
            self.phy = phy
        if chem:
            self.chem = chem
        if math:
            self.math = math
        if bio:
            self.bio = bio

    # def __add__(self, other):
    #     return Student(self.m1+other.m1, self.m2+other.m2, self.m3+other.m3)

    def __str__(self):
        return f"{self.__dict__}"

    def practicals(self):
        if hasattr(self, "chem"):
            print("go to chem lab")
        if hasattr(self, "phy"):
            print("go to phy lab")
        if hasattr(self, "bio"):
            print("go to micobiology lab")

    def test(self, x):
        if isinstance(x, int):
            pass

        if isinstance(x, str):
            pass

        if isinstance(x, float):
            pass


s1 = Student(
    1,
    chem=60,
    math=45,
)
s2 = Student(2, phy=56, math=45)
s3 = Student(3, math=76, bio=89)

s1.practicals()
s2.practicals()
s3.practicals()


print(s1)
print(s2)
print(s3)

# s3 = s1+s2
# print(s3)


def area(*args):
    product = 1
    for i in args:
        product *= i
    return product


print(area(10, 20))
