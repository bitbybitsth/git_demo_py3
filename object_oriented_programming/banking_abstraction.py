from bank_account import BankAccount

from abc import ABC, abstractmethod

ERROR_MESSAGE_KEY = "error_message"


class RBI(ABC):
    @abstractmethod
    def withdraw(self, acc_no, amount):
        pass

    @abstractmethod
    def deposit(self, acc_no, amount):
        pass

    @abstractmethod
    def provide_savings_account(self):
        pass

    @abstractmethod
    def provide_passbook(self):
        pass


class ICICI(RBI):

    accounts = []

    def get_account(self, acc_no):
        for account in ICICI.accounts:
            if account.acc_no == acc_no:
                return account

    def withdraw(self, acc_no, amount):
        pass

    def deposit(self, acc_no, amount):
        pass

    def provide_savings_account(self, acc_no, name, contact):
        account = self.get_account(acc_no)
        if not account:
            HDFC.accounts.append(BankAccount(acc_no, name, 3000, contact))
            return {"status": "Account created"}
        else:
            return {"status": "Account Already exists"}

    def provide_passbook(self):
        pass

    def online_banking(self):
        pass


class HDFC(RBI):

    accounts = []
    NOT_EXISTS_STATUS = {"status": "You don't have account with us"}

    def get_account(self, acc_no):
        for account in HDFC.accounts:
            if account.acc_no == acc_no:
                return account

    def withdraw(self, acc_no, amount):
        account = self.get_account(acc_no)
        if account:
            min_bal = account.balance - amount
            if min_bal > 1000:
                account.balance -= amount
                return {"status": "Amount withdrawed"}
            else:
                print({"status": "you are crossing minimum balance limit"})
                if account.balance - amount < 0:
                    return {"Status": "Insufficient funds"}
                else:
                    account.balance -= amount
                    return {"status": "amount withdrawed"}
        else:
            return HDFC.NOT_EXISTS_STATUS

    def deposit(self, acc_no, amount, pan=None):
        result = self.check_pan_requirement(amount, pan)
        if ERROR_MESSAGE_KEY in result:
            return result

        account = self.get_account(acc_no)
        if account:
            account.balance += amount
            return {"status": "Amount Deposited"}
        else:
            return HDFC.NOT_EXISTS_STATUS

    def check_pan_requirement(self, amount, pan):
        if amount > 50000 and not pan:
            return {ERROR_MESSAGE_KEY: "please provide pan number"}
        return {}

    def open_fix_deposit(self, acc_no, amount, pan=None):
        result = self.check_pan_requirement(amount, pan)
        if ERROR_MESSAGE_KEY in result:
            return result

        print("we have successfully created a FD")

    def provide_passbook(self, acc_no):
        account = self.get_account(acc_no)
        if not account:
            return HDFC.NOT_EXISTS_STATUS

    def provide_savings_account(self, acc_no, name, contact):
        account = self.get_account(acc_no)
        if not account:
            HDFC.accounts.append(BankAccount(acc_no, name, 1000, contact))
            return {"status": "Account created"}
        else:
            return {"status": "Account Already exists"}

    def provide_credit_card(self):
        pass

    @classmethod
    def show_all_acounts(cls):
        print(cls.accounts)


ic = ICICI()
hd = HDFC()


hd.provide_savings_account(121, "salman", "786757565")
print(hd.deposit(121, 500000, pan="sfdsfsdfs"))
print(hd.withdraw(141, 25001))
print(hd.provide_passbook(131))
