"""
Testy dla menedżera lejka sprzedaży i planu follow-up (AAAS Sales Pipeline Manager).
"""
import unittest
import os
from src.sales_pipeline_manager import AAASSalesPipeline

class TestAAASSalesPipeline(unittest.TestCase):
    def setUp(self):
        self.db_path = "docs/test_sales_pipeline.json"
        self.md_path = "docs/test_dashboard.md"
        self.pipeline = AAASSalesPipeline(db_filepath=self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        if os.path.exists(self.md_path):
            os.remove(self.md_path)

    def test_init_and_update(self):
        self.assertEqual(len(self.pipeline.pipeline_leads), 3)
        updated = self.pipeline.update_lead_status("lead_001", "CALL_SCHEDULED", "Przeprowadzenie rozmowy demo")
        self.assertIsNotNone(updated)
        self.assertEqual(updated["status"], "CALL_SCHEDULED")

    def test_dashboard_generation(self):
        md = self.pipeline.generate_dashboard_markdown(self.md_path)
        self.assertTrue(os.path.exists(md))
        with open(md, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Pensjonat Grań", content)
            self.assertIn("MRR", content)

if __name__ == "__main__":
    unittest.main()
