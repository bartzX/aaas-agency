"""
Testy dla agenta Lead Prospector (wyszukiwanie i kwalifikacja pierwszych klientów komercyjnych).
"""
import unittest
import os
from src.lead_prospector_agent import LeadProspector

class TestLeadProspector(unittest.TestCase):
    def setUp(self):
        self.prospector = LeadProspector()

    def test_scan_and_qualify_leads(self):
        leads = self.prospector.scan_and_qualify_leads()
        self.assertEqual(len(leads), 3)
        self.assertEqual(leads[0]["hotelName"], "Pensjonat Syriusz w Karpaczu")
        self.assertGreater(leads[0]["estimatedAnnualOtaCommissionLoss"], 40000.0)

    def test_export_and_report_generation(self):
        self.prospector.scan_and_qualify_leads()
        json_path = self.prospector.export_leads_database("docs/test_leads.json")
        md_path = self.prospector.generate_markdown_report("docs/test_leads.md")
        
        self.assertTrue(os.path.exists(json_path))
        self.assertTrue(os.path.exists(md_path))
        
        # Sprzątanie plików testowych
        if os.path.exists(json_path):
            os.remove(json_path)
        if os.path.exists(md_path):
            os.remove(md_path)

if __name__ == "__main__":
    unittest.main()
