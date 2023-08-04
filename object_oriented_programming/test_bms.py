import unittest
from datetime import datetime
from typing import Any

from bms import BMS
from movies import Movie

# @unittest.skip("showing class skipping")
class TestBooking(unittest.TestCase):
    def setUp(self):
        print("setup called")
        self.bm = BMS()
        radhe = Movie(1, "radhe", datetime(2021, 6, 4, 22), "salman", "disha", 300.0)
        challang = Movie(
            2, "challang", datetime(2021, 6, 4, 12), "raj kumar", "nusharat", 250.0
        )
        self.bm.create(movie=radhe)
        self.bm.create(movie=challang)

    def tearDown(self):
        print("after test case")

    def test_booking_successful(self):
        print("first test case")
        self.assertEqual(
            self.bm.book_tickets(2, 5, 4, 5, 6, 7, 8),
            "tickets booked please pay 1250.0",
        )

    # @unittest.skip("demonstrating skipping")
    @unittest.expectedFailure
    def test_booking_given_seats_not_available(self):
        print("seconf test case")
        self.bm.book_tickets(1, 5, 4, 5, 6, 7, 8)
        self.assertEqual(
            self.bm.book_tickets(1, 10, 4, 5, 6, 7, 8),
            "10 sea are not available, we ar left wth      only 5 **seats##",
        )

    def test_booking_show_not_available(self):
        print("third test case")
        self.assertEqual(
            self.bm.book_tickets(4, 10, 4, 5, 6, 7, 8), "we are not showing this movie"
        )

if __name__ == '__main__':
    unittest.main()