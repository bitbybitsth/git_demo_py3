import test_bms

class BankAccount:
    def __init__(self, acc_no, name, balance, contact):
        self.acc_no = acc_no
        self.acc_holder = name
        self.balance = balance
        self.contact = contact

    def __str__(self):
        return f"{self.acc_no} - {self.acc_holder} - {self.balance}"

    def __repr__(self):
        return str(self)
