import logging
from my_loggers import get_laptop_loogers
import employee

lap_log = get_laptop_loogers()

# logging.basicConfig(level=10, filename="laptop.log", format="%(asctime)s -> %(message)s in -> file=%(filename)s")


class Laptop:

    def __init__(self, lid, brand):
        self.id = lid
        self.brand = brand
        lap_log.debug(f"Laptop of {brand} created")


l1= Laptop(1,"HP")
l2= Laptop(3,"Dell")
l3= Laptop(3,"lenevo")


