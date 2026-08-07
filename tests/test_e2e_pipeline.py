"""
Testy dla pełnego potoku E2E (End-to-End) oraz scenariuszy elastyczności biznesowej agencji AAAS.
"""
import unittest
from src.e2e_pipeline import E2EBookingPipeline

class TestE2EPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = E2EBookingPipeline(agency_name="AAAS Agency")

    def test_full_e2e_simulation(self):
        report = self.pipeline.run_full_e2e_simulation()
        self.assertEqual(report["status"], "100%_TESTED_SUCCESS")
        
        webhook_data = report["step2_ai_receptionist_webhook"]
        self.assertEqual(webhook_data["totalPrice"], 1020)
        self.assertEqual(webhook_data["petFee"], 0)
        self.assertEqual(webhook_data["petSavings"], 150)
        
        crm_data = report["step3_crm_record"]
        self.assertEqual(crm_data["deal_value"], 1020)
        self.assertEqual(crm_data["stage"], "CONFIRMED_DIRECT_BOOKING")
        
        alert_data = report["step4_owner_alert"]
        self.assertIn("NOWA REZERWACJA BEZPOŚREDNIA", alert_data["title"])
        
        roi_data = report["step5_commercial_roi"]
        self.assertEqual(roi_data["savedOtaCommission18Percent"], 3375.0)
        self.assertEqual(roi_data["hotelNetProfitIncrease"], 1876.0)
        self.assertEqual(roi_data["agencyAnnualMRRFromClient"], 17988.0)

    def test_business_flexibility_scenarios(self):
        # Scenariusz A: Sama strona
        res_a = self.pipeline.simulate_website_only_purchase("Pensjonat Syriusz", setup_fee=4900.0)
        self.assertEqual(res_a["scenario"], "WEBSITE_ONLY_STANDALONE")
        self.assertEqual(res_a["upfrontRevenueToAgency"], 4900.0)
        self.assertEqual(res_a["formMode"], "STANDARD_EMAIL_FALLBACK")

        # Scenariusz B: Zamrożenie sezonowe
        res_b = self.pipeline.simulate_seasonal_pause("Pensjonat Syriusz", full_mrr=1499.0, sleep_mrr=299.0)
        self.assertEqual(res_b["scenario"], "SEASONAL_SLEEP_MODE")
        self.assertEqual(res_b["newSleepMRR"], 299.0)

        # Scenariusz C: Raport Koń Trojański po 60 dniach
        res_c = self.pipeline.simulate_upsell_report_after_60_days("Pensjonat Syriusz", missed_leads=8, avg_val=750.0)
        self.assertEqual(res_c["scenario"], "TROJAN_HORSE_UPSELL_REPORT")
        self.assertEqual(res_c["estimatedLostRevenue"], 6000.0)

if __name__ == "__main__":
    unittest.main()
