from datetime import datetime, timedelta

from movies import Movie

all_movies = []

from typing import Any, Union, Sequence


class BMS:

    hour_24 = timedelta(hours=24)
    hour_12 = timedelta(hours=12)
    hour_3 = timedelta(hours=3)

    def read(self, mid: int) -> Movie:
        for movie in all_movies:
            if movie.mid == mid:
                return movie

    def create(self, movie: Movie) -> None:
        all_movies.append(movie)

    def remove(self, mid: int) -> None:
        movie = self.read(mid)
        if movie:
            all_movies.remove(movie)
        else:
            print("no movie present")

    def update(self, mid: int, movie: Movie) -> None:
        db_movie = self.read(mid)
        if movie:
            db_movie.name = movie.name
        else:
            print("no movie present")

    def book_tickets(self, mid: int, qty: int, *seat_no: int) -> Union[str, dict]:
        """
        used for ticket booking
        :param mid (int): unique id of the movie
        :param qty: total no of ticket to be booked
        :param seat_no: seat nos to be booked
        :return: status of the operation
        """
        movie = self.read(mid)
        if movie:
            vacant_seats = [
                key for key, value in movie.tickets.items() if value == "vacant"
            ]
            if len(vacant_seats) > qty:
                for seat in seat_no:
                    if seat not in vacant_seats:
                        return f"seat no {seat} is not available"
                else:
                    for seat in seat_no:
                        movie.tickets[seat] = "booked"
                    return f"tickets booked please pay {qty*movie.price}"
            else:
                return f"{qty} seats are not available, we are left with only {len(vacant_seats)} seats"
        else:
            return {"status": "we are not showing this movie"}

    def cancel_ticket(self, mid, *seat_no):
        cancelled = False
        movie = self.read(mid)
        if movie:
            booked_tickets = [
                key for key, value in movie.tickets.items() if value == "booked"
            ]
            for seat in seat_no:
                if seat in booked_tickets:
                    movie.tickets[seat] = "vacant"
                    cancelled = True
                else:
                    print(f"{seat} is not booked")
            if cancelled:
                now = datetime.now()
                diff = movie.show_timimg - now
                if diff >= BMS.hour_24:
                    return_amnt = movie.price - movie.price * 0.25
                    print(return_amnt * len(seat_no))
                elif diff >= BMS.hour_12:
                    return_amnt = movie.price - movie.price * 0.50
                    print(return_amnt * len(seat_no))
                elif diff >= BMS.hour_3:
                    return_amnt = movie.price - movie.price * 0.75
                    print(return_amnt * len(seat_no))

        else:
            print("not present")


#
#
radhe = Movie(1, "radhe", datetime(2021, 6, 4, 22), "salman", "disha", 300.0)
challang = Movie(
    2, "challang", datetime(2021, 6, 4, 12), "raj kumar", "nusharat", 250.0
)
# sholay = Movie(3, "Sholay", datetime(2021,6,4,22), "dharmendra", "hema", 400.0)
# #
bms = BMS()
bms.create(radhe)
bms.create(challang)
# # bms.create(sholay)
# #
print(radhe.tickets)
bms.book_tickets(1, 4, 4, 5, 6, 7)
print(radhe.tickets)
# # bms.book_tickets(1,2,2,5)
# # print(radhe.tickets)
# #
# # bms.cancel_ticket(1, 4, 5)
#
#
#
#
#
#
#
#
# # vacant_seats = [key for key, value in movie.tickets.items() if value=="vacant"]
#
#
#
#
#
#
#
#
#
#
# # vacant_seats = []
# # tickets = {1: 'vacant', 2: 'vacant', 3: 'vacant', 4: 'vacant', 5: 'vacant', 6: 'vacant', 7: 'vacant', 8: 'vacant', 9: 'vacant', 10: 'vacant'}
# # for key, value in tickets.items():
# #     if value == "vacant":
# #         vacant_seats.append(key)
# #
# # print(vacant_seats)
# # print(len(vacant_seats))
