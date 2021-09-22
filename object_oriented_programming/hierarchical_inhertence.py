# when every class is inherited from a single base class then it is called as hierarchical inheritence.
# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B): pass
# class E(B): pass
# class F(C): pass
# class G(C): pass


class Cricket:
    ground = "MCA"


class T20(Cricket):
    overs = 40


class OneDay(Cricket):
    overs = 100


class Test(Cricket):
    overs = 450


class WomensT20(T20):
    pass


class MensT20(T20):
    pass


class WomensOD(OneDay):
    pass


class MensOD(OneDay):
    pass


class WomensTest(Test):
    pass


class Mens(Test):
    pass


class U19(WomensT20):
    pass


class U21(WomensOD):
    pass


u1 = U21()
print(help(u1))
