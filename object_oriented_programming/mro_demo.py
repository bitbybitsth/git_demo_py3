"""
Method Resolution Order:  it is an order which is used to determine a method definition in case of inheritence.

C3 algorithm is used to determine method resolution order
"""


class O:
    pass


class D(O):
    pass


class E(O):
    pass


class F(O):
    pass


class B(D, E):
    pass


class C(D, F):
    pass


class A(B, C):
    pass


a = A()

a.display()

# print(help(a))
