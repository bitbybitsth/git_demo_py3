import logging
import laptop
from my_loggers import get_emp_logger

emp_logger = get_emp_logger()

class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        emp_logger.info(f"Employee {name} created")


e1 = Employee(id=1,name="evan")
e2 = Employee(id=2, name="rock")
e3 = Employee(id=3, name="john")


