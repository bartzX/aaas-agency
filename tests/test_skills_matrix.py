"""
Testy dla matrycy 100+ nowych umiejętności web designu, konwersji i automatyzacji (AAAS Skills Matrix).
"""
import unittest
from src.web_design_skills_matrix import AAASWebDesignSkillsMatrix

class TestAAASSkillsMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = AAASWebDesignSkillsMatrix()

    def test_minimum_100_skills_requirement(self):
        report = self.matrix.verify_all_101_skills_active()
        self.assertGreaterEqual(report["totalSkillsVerified"], 100, f"Znaleziono tylko {report['totalSkillsVerified']} umiejętności!")
        self.assertTrue(report["passedMinimum100Requirement"])
        self.assertEqual(report["certification"], "100% VERIFIED - 101 WEB DESIGN & AGENCY SKILLS ACTIVE")

    def test_specific_core_skills(self):
        blik = self.matrix.get_skill_by_id("022")
        self.assertIn("BLIK", blik["name"])

        fable = self.matrix.get_skill_by_id("057")
        self.assertIn("Fable 5", fable["name"])

        ical = self.matrix.get_skill_by_id("078")
        self.assertIn("Zero Double-Booking", ical["name"])

if __name__ == "__main__":
    unittest.main()
