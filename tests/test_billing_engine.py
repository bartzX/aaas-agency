"""
Testy dla kalkulatora płatności, abonamentów i kosztów API AI (AAAS Billing Engine).
"""
import unittest
from src.billing_engine import AAASBillingEngine

class TestAAASBillingEngine(unittest.TestCase):
    def setUp(self):
        self.billing = AAASBillingEngine()

    def test_calculate_ai_token_cost(self):
        cost = self.billing.calculate_ai_token_cost(monthly_inquiries=500)
        self.assertEqual(cost["totalTokensUsed"], 1_000_000)
        self.assertEqual(cost["totalCostPLN"], 0.60) # 0.15 USD * 4.0 PLN
        self.assertLess(cost["costPerInquiryPLN"], 0.01)

    def test_client_invoice_and_margin(self):
        report = self.billing.generate_client_invoice_and_margin_report(
            client_name="Pensjonat Grań",
            monthly_mrr_fee_pln=1499.0,
            monthly_inquiries=500
        )
        self.assertEqual(report["clientName"], "Pensjonat Grań")
        self.assertGreater(report["agencyOperatingMarginPercent"], 98.0)
        self.assertGreater(report["agencyNetProfitPLN"], 1480.0)

if __name__ == "__main__":
    unittest.main()
