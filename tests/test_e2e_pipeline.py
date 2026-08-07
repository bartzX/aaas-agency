"""
Testy dla pełnego potoku E2E (End-to-End) agencji AAAS.
"""
import unittest
from src.e2e_pipeline import E2EBookingPipeline

class TestE2EPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = E2EBookingPipeline(agency_name="AAAS Agency")

    def test_full_e2e_simulation(self):
        report = self.pipeline.run_full_e2e_simulation()
        self.assertEqual(report["status"], "100%_TESTED_SUCCESS")
        
        # Weryfikacja kalkulacji ceny w Webhooku n8n (3 noce pokój studio 340 zł/doba = 1020 zł)
        webhook_data = report["step2_ai_receptionist_webhook"]
        self.assertEqual(webhook_data["totalPrice"], 1020)
        self.assertEqual(webhook_data["petFee"], 0)
        self.assertEqual(webhook_data["petSavings"], 150) # 3 noce * 50 zł za psa
        
        # Weryfikacja rekordu CRM
        crm_data = report["step3_crm_record"]
        self.assertEqual(crm_data["deal_value"], 1020)
        self.assertEqual(crm_data["stage"], "CONFIRMED_DIRECT_BOOKING")
        
        # Weryfikacja alertu SMS/Telegram
        alert_data = report["step4_owner_alert"]
        self.assertIn("NOWA REZERWACJA BEZPOŚREDNIA", alert_data["title"])
        
        # Weryfikacja ROI Agencji i Klienta
        roi_data = report["step5_commercial_roi"]
        self.assertEqual(roi_data["savedOtaCommission18Percent"], 3375.0) # 18% z 18,750 zł
        self.assertEqual(roi_data["hotelNetProfitIncrease"], 1876.0) # 3375 zł - 1499 zł MRR
        self.assertEqual(roi_data["agencyAnnualMRRFromClient"], 17988.0) # 1499 zł * 12

if __name__ == "__main__":
    unittest.main()
