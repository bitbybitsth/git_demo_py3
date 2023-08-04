"""
class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):
    pass

"""


class College:
    ground = ""
    auditorium = ""

    def book_auditoium(self):
        pass

    def book_ground(self):
        if not College.ground:
            College.ground = f"booked by {self.__class__}"
        else:
            print("already booked")

    def release_ground(self):
        if College.ground:
            College.ground = ""
        else:
            print("it is not booked")


class EngineeringDepartment(College):
    library = ""

    def book_library(self):
        pass


class ITDept(EngineeringDepartment):
    labs = ""

    def book_lab(self):
        pass


class MechnicalDepartnet(EngineeringDepartment):
    workshop = ""

    def book_workshop(self):
        pass


me_ty = MechnicalDepartnet()


it_fy = ITDept()
it_fy.book_ground()
print(College.ground)
it_fy.book_library()
it_fy.book_lab()
it_fy.book_auditoium()

ed = EngineeringDepartment()
ed.book_auditoium()
ed.book_ground()


class A:
    pass


a = A()

a.__dict__
