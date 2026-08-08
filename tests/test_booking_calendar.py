"""
Testy dla silnika weryfikacji dostępności i synchronizacji kalendarzy iCal (AAAS Booking Calendar Engine).
"""
import unittest
from src.booking_calendar_engine import AAASBookingCalendarEngine

class TestAAASBookingCalendarEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AAASBookingCalendarEngine(hotel_name="Pensjonat Grań")

    def test_available_dates(self):
        res = self.engine.verify_room_availability("studio", "2026-09-01", "2026-09-05")
        self.assertTrue(res["available"])
        self.assertEqual(res["status"], "TERMIN_WOLNY_MOZNA_REZERWOWAC")

    def test_blocked_dates_overlap_and_suggestion(self):
        # Pokój studio ma zajęty termin 2026-08-15 - 2026-08-18
        res = self.engine.verify_room_availability("studio", "2026-08-16", "2026-08-19")
        self.assertFalse(res["available"])
        self.assertEqual(res["status"], "TERMIN_ZAJETY_ZABLOKOWANY_NA_STRONIE")
        self.assertEqual(res["suggestedAlternative"]["checkIn"], "2026-08-18")

    def test_get_blocked_dates_for_ui(self):
        blocked = self.engine.get_blocked_dates_for_calendar_ui("studio")
        self.assertIn("2026-08-15", blocked)
        self.assertIn("2026-08-16", blocked)
        self.assertIn("2026-08-17", blocked)
        self.assertNotIn("2026-08-18", blocked) # dzień wymeldowania jest już wolny dla kolejnego gościa

if __name__ == "__main__":
    unittest.main()
