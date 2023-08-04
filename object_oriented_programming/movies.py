"""movies class, some fileds, crud, book ticket aur cancel ticket
book ticket , more than one ticket
cancel me rahega, ki 3 gnahte pahile cancel kiya toh 75% dedecution
12 gnahte pahile 50
24+ - 25"""
from datetime import datetime


class Movie:
    def __init__(self, mid, name, show_timing, actor, actress, price):
        self.mid = mid
        self.name = name
        self.show_timimg = show_timing
        self.actor = actor
        self.actress = actress
        self.price = price
        t = list(range(1, 11))
        self.tickets = dict.fromkeys(t, "vacant")

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)
