"""
Testy dla audytora gotowości komercyjnej (AAAS Comprehensive Readiness Audit).
"""
import unittest
from src.comprehensive_test_suite import AAASReadinessAudit

class TestComprehensiveReadiness(unittest.TestCase):
    def setUp(self):
        self.auditor = AAASReadinessAudit()

    def test_live_urls(self):
        results = self.auditor.test_live_urls()
        self.assertGreaterEqual(len(results), 5)
        for res in results:
            self.assertTrue(res["success"], f"Adres {res['url']} zwrócił błąd: {res.get('status_code')}")

    def test_n8n_workflows(self):
        workflows = self.auditor.verify_n8n_workflows()
        self.assertEqual(len(workflows), 3)
        for wf in workflows:
            self.assertTrue(wf["valid"], f"Przepływ {wf['file']} jest nieprawidłowy")

    def test_outreach_compliance(self):
        comp = self.auditor.verify_outreach_compliance()
        self.assertTrue(comp["exists"])
        self.assertTrue(comp["has_nationwide_scope"], "Brak zasięgu 'w całej Polsce'")
        self.assertTrue(comp["has_pl_domain_standard"], "Brak standardu domeny .pl")
        self.assertTrue(comp["has_photo_disclaimer"], "Brak uwagi o wymianie zdjęć AI")

    def test_overall_readiness(self):
        report = self.auditor.run_complete_readiness_audit()
        self.assertEqual(report["overallReadiness"], "100% READY FOR COMMERCIAL LAUNCH")
        self.assertGreaterEqual(float(report["agencyOperatingMargin"].replace("%", "")), 98.0)

if __name__ == "__main__":
    unittest.main()
