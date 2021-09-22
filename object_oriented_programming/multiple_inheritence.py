# When one child is inherting properties of more than one parent is called as multiple inheritence

# one derived class multiple base class
#
# class A:
#     pass
#
# class B:
#     pass
#
# class C(A,B):
#     pass


class India:
    def __init__(self, contract):
        print("test")
        self.contract = contract

    def spices(self):
        print("we will provide you export quality spices")


class Israel:
    def __init__(self, contract):
        print("israel")
        self.contract = contract

    def farming_technology(self):
        print("We are providing best in class technology")


class Africa(India, Israel):
    def __init__(self):
        # super().__init__(True)
        India.__init__(self, True)
        Israel.__init__(self, False)


af = Africa()

print(af.contract)
af.spices()
af.farming_technology()
