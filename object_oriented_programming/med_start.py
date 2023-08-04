from crud_operations_medicine import Medicine
from datetime import date

all_medicines = []


class MedicineCRUDImplementor:

    # def crearte_med(self,mid, name, cost, exp_date, mfg_date, manfacturer, qty):
    #     med = Medicine(mid, name, cost, exp_date, mfg_date, manfacturer, qty)
    #     all_medicines.append(med)

    def create(self, med):
        all_medicines.append(med)

    def read(self, mid):
        for medicine in all_medicines:
            if medicine.mid == mid:
                return medicine

    def update(self, med, mid):
        for medicine in all_medicines:
            if medicine.mid == mid:
                medicine.name = med.name
                medicine.price = med.price
                medicine.mfg_date = med.mfg_date
                medicine.exp_date = med.exp_date
                medicine.manufacturer = med.manufacturer
                medicine.qty = med.qty

    def remove(self, mid):
        for medicine in all_medicines:
            if medicine.mid == mid:
                all_medicines.remove(medicine)

    def read_all(self):
        for medicine in all_medicines:
            print(medicine)


crocin = Medicine(1, "crocin", 10, date(2022, 1, 1), date(2019, 1, 1), "cipla", 5)

disprin = Medicine(2, "disprin", 15, date(2021, 10, 10), date(2019, 1, 1), "mankind", 5)

limcee = Medicine(3, "limcee", 20, date(2023, 1, 1), date(2019, 1, 1), "abbot", 20)


mci = MedicineCRUDImplementor()
mci.create(crocin)
mci.create(disprin)
mci.create(limcee)


med = mci.read(3)
print("fetched using id", med)
print(med)
mci.read_all()


# mci.remove(2)
# print("after remove")
# mci.read_all()
#
# med = Medicine(2, "Dispriano", 30,date(2021,10,10),
#                   date(2019,1,1), "mankind", 50)
#
#
# mci.update(med, 2)
# print("After update")
# mci.read_all()
#
#
