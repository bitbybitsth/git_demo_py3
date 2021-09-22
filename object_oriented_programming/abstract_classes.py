from abc import ABC, abstractmethod


class Ecommerce(ABC):
    @abstractmethod
    def online_payment(self, amount):
        pass

    @abstractmethod
    def cart(self, product):
        pass

    @abstractmethod
    def delivery(self, address):
        pass

    @abstractmethod
    def returns(self, product, address):
        pass

    def search_product(self):
        pass

    def give_ratings(self):
        pass

    def cash_on_delivery(self):
        pass


class Flipkart(Ecommerce):
    pass


class Amazon(Ecommerce):
    pass


class Myntra(Ecommerce):
    def online_payment(self, amount):
        pass

    def returns(self, product, address):
        pass

    def cart(self, product):
        pass

    def delivery(self, address):
        pass

    def fashion_products_only(self):
        pass


m1 = Myntra()
m1.cash_on_delivery()

f = Flipkart()
