class BaseProduct:

    all_products = []

    def __init__(self, pid, name, price, qty):
        self.pid = pid
        self.name = name
        self.price = price
        self.qty = qty

    def create(self):
        BaseProduct.all_products.append(self)

    def get_product(self, pid):
        for product in BaseProduct.all_products:
            if product.pid == pid:
                return product

    def sell_product(self, pid, qty):
        product = self.get_product(pid)
        if product:
            if qty <= product.qty:
                amount = product.price * qty
                return {"status": f"Product sold at {amount}"}, product
            else:
                return {"error_message": "Given Quantity not available"}, product
        else:
            return {"error_message": f"Prouduct with id {pid} not available"}, None

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

    @classmethod
    def display_products(cls):
        print(cls.all_products)


class Electronics(BaseProduct):
    def __init__(self, pid, name, price, qty):
        super().__init__(pid, name, price, qty)

    def sell_product(self, pid, qty):
        resp = super().sell_product(pid, qty)
        if "error_message" not in resp[0]:
            amount = resp[1].price * 0.95
            return {"status": f"total amount {amount}"}
        else:
            return resp[0]

        # product = self.get_product(pid)
        # if product:
        #     if qty <= product.qty:
        #         amount = (product.price*0.95) * qty
        #         return {"status": f"Product sold at {amount}"}
        #     else:
        #         return {"error_message": "Given Quantity not available"}
        # else:
        #     return {"error_message": f"Prouduct with id {pid} not available"}


class Clothing(BaseProduct):
    def __init__(self, pid, name, price, qty):
        super().__init__(pid, name, price, qty)

    def sell_product(self, pid, qty):
        product = self.get_product(pid)
        if product:
            if qty <= product.qty:
                amount = (product.price * 1.05) * qty
                return {"status": f"Product sold at {amount}"}
            else:
                return {"error_message": "Given Quantity not available"}
        else:
            return {"error_message": f"Prouduct with id {pid} not available"}


p1 = Electronics(1, "iron", 1500, 5)
p1.create()
print(p1.sell_product(1, 10))


c1 = Clothing(2, "Jakcet", 1500, 10)
c1.create()

print(c1.sell_product(2, 3))

# BaseProduct.sell_product(c1,2,3)

BaseProduct.display_products()
