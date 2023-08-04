import datetime


class Medicine:
    def __init__(self, mid, name, cost, exp_date, mfg_date, manfacturer, qty):
        self.mid = mid
        self.name = name
        self.price = cost
        self.exp_date = exp_date
        self.mfg_date = mfg_date
        self.manufacturer = manfacturer
        self.qty = qty

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        self.qty += other.qty

    def __sub__(self, other):
        if self.exp_date > datetime.datetime.now():
            self.qty -= other.qty

    def __mul__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __gt__(self, other):
        if self.exp_date > other.exp + datetime:
            return True
        return False

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass


disprin = Medicine(
    2, "disprin", 15, datetime(2021, 5, 10), datetime(2019, 1, 1), "mankind", 5
)

limcee = Medicine(
    mid=3,
    exp_date=datetime(2020, 1, 1),
    mfg_date=datetime(2021, 1, 1),
    name="limcee",
    qty=5,
    manfacturer="cipla",
    cost=2,
)

print(limcee+disprin)