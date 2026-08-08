"""
Testy dla agenta Lead Prospector (wyszukiwanie i kwalifikacja pierwszych klientów komercyjnych)
oraz pakietów sprzedażowych i strategii domknięcia dla Pensjonatu Grań.
"""
import unittest
import os
import json
from src.lead_prospector_agent import LeadProspector

class TestLeadProspector(unittest.TestCase):
    def setUp(self):
        self.prospector = LeadProspector()

    def test_scan_and_qualify_leads(self):
        leads = self.prospector.scan_and_qualify_leads()
        self.assertEqual(len(leads), 3)
        self.assertEqual(leads[0]["hotelName"], "Pensjonat Syriusz w Karpaczu")
        self.assertGreater(leads[0]["estimatedAnnualOtaCommissionLoss"], 40000.0)
        self.assertEqual(leads[1]["hotelName"], "Pensjonat Grań")

    def test_export_and_report_generation(self):
        self.prospector.scan_and_qualify_leads()
        json_path = self.prospector.export_leads_database("docs/test_leads.json")
        md_path = self.prospector.generate_markdown_report("docs/test_leads.md")
        
        self.assertTrue(os.path.exists(json_path))
        self.assertTrue(os.path.exists(md_path))
        
        if os.path.exists(json_path):
            os.remove(json_path)
        if os.path.exists(md_path):
            os.remove(md_path)

    def test_pensjonat_gran_workflow_and_outreach(self):
        wf_path = "workflows/03_pensjonat_gran_ski_receptionist.json"
        self.assertTrue(os.path.exists(wf_path), "Brak pliku workflow n8n dla Pensjonatu Grań")
        with open(wf_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data["nodes"]), 4)
            self.assertIn("Grań", data["name"])
            
        outreach_path = "docs/OUTREACH_PENSJONAT_GRAN.md"
        self.assertTrue(os.path.exists(outreach_path), "Brak raportu z pakietem dla Pensjonatu Grań")
        with open(outreach_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Kolorowa 3", content)
            self.assertIn("601 584 872", content)

    def test_pensjonat_gran_closing_strategy(self):
        strategy_path = "docs/STRATEGIA_DOMKNIECIA_PENSJONAT_GRAN.md"
        self.assertTrue(os.path.exists(strategy_path), "Brak strategii domknięcia dla Pensjonatu Grań")
        with open(strategy_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Hotel Kolorowa", content)
            self.assertIn("14 dni", content)
            self.assertIn("3–4 bezpośrednich rezerwacjach", content)

if __name__ == "__main__":
    unittest.main()
