"""
Testy dla schematu sprawdzania wdrożenia L&B Spa pod nadzorem Project Managera (AAAS PM Scheme).
"""
import unittest
from src.pm_lb_spa_verifier import ProjectManagerLBSpaAuditor

class TestProjectManagerLBSpa(unittest.TestCase):
    def setUp(self):
        self.auditor = ProjectManagerLBSpaAuditor()

    def test_pm_authenticity_schema(self):
        report = self.auditor.execute_pm_authenticity_schema()
        self.assertTrue(report["passed"], f"Audyt PM nie powiódł się: {report}")
        self.assertEqual(report["pm_certification"], "100% APPROVED BY PROJECT MANAGER - UNIQUE LUXURY DESIGN")

if __name__ == "__main__":
    unittest.main()
