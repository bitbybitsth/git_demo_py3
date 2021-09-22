import logging
from crud_operations_medicine import Medicine
from datetime import datetime
from medicines_exceptions import MedicineExpired

logging.basicConfig(
    level=logging.DEBUG, filename="medicine.log", format="%(asctime)s -> %(message)s"
)

all_medicines = []


class MedicineCRUDImplementor:

    # def crearte_med(self,mid, name, cost, exp_date, mfg_date, manfacturer, qty):
    #     med = Medicine(mid, name, cost, exp_date, mfg_date, manfacturer, qty)
    #     all_medicines.append(med)

    def create(self, med):
        logging.info(f"{med.name} created succesfully")
        all_medicines.append(med)

    def read(self, mid):
        for medicine in all_medicines:
            if medicine.mid == mid:
                return medicine

    def update(self, med, mid):
        m = self.read(mid)
        if m:
            m.name = med.name
            m.price = med.price
            m.mfg_date = med.mfg_date
            m.exp_date = med.exp_date
            m.manufacturer = med.manufacturer
            m.qty = med.qty
            logging.info(f"{m.id} -> {m.name} updated succesfully")
            return {"status": "Medicine updated successfully"}
        else:
            logging.debug(f"medicine with {mid} not present in database")
            return {"error_message": "Medicine not present in database"}

    def remove(self, mid):
        m = self.read(mid)
        if m:
            all_medicines.remove(m)
            logging.info(f"{m.id} -> {m.name} deleted successfully")
            return {"status": "Medicine Deleted Successfully"}
        else:
            logging.debug(f"medicine with {mid} not present in database")
            return {"error_message": "medicine not present in database"}

    def read_all(self):
        print(all_medicines)

    def sell_medicine(self, mid, qty, bill):
        med = self.read(mid)
        if med:
            now = datetime.now()
            if med.exp_date > now:
                if med.qty >= qty:
                    amnt = med.price * qty
                    if amnt <= bill:
                        med.qty -= qty
                    else:
                        print(f"{bill} is not sufficient please give more {amnt-bill}")
                    print(f"Please pay {amnt}")
                else:
                    logging.debug(
                        f"Medicine quantity getting reduced, order more if needed, requested qty {qty}"
                    )
                    print("We don't have that quantity")
            else:
                logging.error(f"{med.name} -> {med.mid} is expired replcae immedtaely")
                raise MedicineExpired()
        else:
            print("Medicine not available")

    def stock_update(self, med):
        st_med = self.read(med.mid)
        if st_med:
            st_med.qty += med.qty
        else:
            self.create(med)

    def stock_check(self, check_qty):
        for medicine in all_medicines:
            if medicine.exp_date < datetime.now():
                print(f"{medicine.name} is expired please replace")
            if medicine.qty <= check_qty:
                logging.critical(f"{medicine.name} will be exhausted order more")
                print(f"{medicine.name} is low in quantity")


crocin = Medicine(
    1, "crocin", 10, datetime(2022, 1, 1), datetime(2019, 1, 1), "cipla", 20
)

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


mci = MedicineCRUDImplementor()
mci.create(crocin)
mci.create(disprin)
mci.create(limcee)

mci.sell_medicine(3, 1, 50)

# mci.sell_medicine(1, 4,50)
# mci.sell_medicine(1, 4, 20)
# mci.sell_medicine(44, 100, 4)
# mci.sell_medicine(3, 50,50)
# mci.sell_medicine(2,2,50)


#
# med = Medicine(3, "limcee", 20,datetime(2023,1,1),
#                   datetime(2024,1,1), "abbot", 20)
#

# mci.stock_update(med)
# mci.stock_check(5)
# print(mci.read(3))
# mci.read_all()


# # mci.read_all()
# #
# # med = mci.read(54)
# # print("fetched using id", med)
# # mci.read_all()
#
# # mci.remove(2)
# #
# # print("after remove")
# # mci.read_all()
# #
# med = Medicine(2, "Dispriano", 30,datetime(2021,10,10),
#                   datetime(2019,1,1), "mankind", 50)
# #
# #
# operation_status = mci.update(med, 22)
# print(operation_status)
# #
# #
#
# # med = mci.read(55)
# # print(med)
# # status = mci.remove(3)
# # print(status)
#
