class TataCar:
    def __init__(self, model, engine):
        self.model = model
        self._engine = engine
        self.__cylinder = 1000

    def display(self):
        print(self.model)

    def install_engine(self):
        print(f"setting up {self._engine}")

    def __replace_engine(self):
        print("replace engine")

    def check_cylinder(self):
        print(f"cylinder is of cc {self.__cylinder}")


class RegistereDealer(TataCar):
    def get_engine_replaced(self):
        super()._replace_engine()


nexon = TataCar("top end", "V4")
# # public access modifiers
# nexon.display()
# print(nexon.model)
# nexon.model = "mid end"
# print(nexon.model)

# # Protected
# print(nexon._engine)
# nexon._replace_engine()

# private

nexon.check_cylinder()
# print(nexon.__cylinder)
print(nexon._TataCar__cylinder)
nexon._TataCar__cylinder = 2000
print(nexon._TataCar__cylinder)

li = [10, 4443, 34, 677, 78, 34, 67, 23, 56, 34, 67, 89, 67, 78, 67, 34, 54, 34, 56, 34]
import collections

print(collections.Counter(li))

d = {}
for num in li:
    if num not in d:
        d[num] = 1
    else:
        d[num] = d[num] + 1

for num in li:
    if num not in d:
        d[num] = li.count(num)


# print(d)
