from datetime import datetime


class Car:
    def __init__(self, model, year, mileage, cost, brand, color, engine_type="Diesel"):
        self.model = model
        self.year = year
        self.mileage = mileage
        self.cost = cost
        self.brand = brand
        self.color = color
        self.type = engine_type
        self.insured = False
        self.accessories = ["mirror", "stickers", "covers"]

    # def get_age(self):
    #     pass

    def purchase_Accessories(self, *args):
        self.accessories.extend(args)

    def avail_insurance(self):
        self.insured = True

    def purchase(self):
        if self.brand.lower().strip() == "tata":
            self.cost -= self.cost * 0.15

        if not self.insured:
            self.avail_insurance()

        print(f"Congratulations on purchasing a {self.color} {self.brand} {self.model}")
        print(f"Please Pay {self.cost} asap")

    def service(self):
        if not self.insured:
            self.avail_insurance()

    def __str__(self):
        s = ""
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                s += f"{key}: {','.join(value)}"
            else:
                s += f"{key}: {value}\n"
        # return f"Brand: {self.brand}\nModel:{self.model}\nColor:{self.color}\nManufactured:{self.year}\n" \
        #        f"Cost: {self.cost}\nMileage: {self.mileage}\nType:{self.type},\nAccessories: {','.join(self.accessories)}\n---
        return s


i20 = Car("i20", datetime(2020, 1, 1), 21, 700000.0, "hundayi", "black", "Petrol")
fortuner = Car("fortuner", datetime(2019, 1, 1), 13, 2500000.0, "Toyota", "white")

nexon = Car(
    brand="       TATA        ",
    color="blue",
    mileage=20,
    model="Nexon",
    year=datetime(2021, 1, 1),
    cost=500000.0,
)

i20.purchase()
fortuner.purchase()
nexon.purchase()
#
fortuner.bullet_proof_glass = True
#
# print(nexon.accessories)
nexon.purchase_Accessories("tail lamp", "music suytem", "wheel cover")
# print(nexon.accessories)
#
# print(type(i20))
# print(type(fortuner))
# print(type(nexon))

num = 10
avg = 45.6
message = "hello"
c1 = Car("i10", datetime(2020, 1, 1), 21, 700000.0, "hundayi", "black", "Petrol")

# print(num)
# print(avg)
# print(message)
print(c1)
print(fortuner)
print(i20)
print(nexon)
# c1.display_details()

print(isinstance(num, int))
print(isinstance(avg, str))
print(isinstance(nexon, Car))
print(isinstance(fortuner, datetime))
x = datetime.now()
print(isinstance(x, datetime))


def date_formatting(now):
    format = "%Y-%m-%d %H:%M:%S"
    return now.strftime(format)
