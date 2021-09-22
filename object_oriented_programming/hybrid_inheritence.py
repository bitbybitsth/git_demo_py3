from multiple_inheritence import India, Israel
from single_inheritance import Employee
from multilevel_inheritence import EngineeringDepartment, MechnicalDepartnet, ITDept


class HybridDemo(EngineeringDepartment, Employee):
    pass


class Hybrid2(India, HybridDemo, ITDept):
    pass


class A(HybridDemo):
    pass


class B(A):
    pass


class C(B):
    pass
