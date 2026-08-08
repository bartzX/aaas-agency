"""
Testy dla matrycy 150+ nowych umiejętności web designu, konwersji, 3D i automatyzacji (AAAS Next-Gen Skills Matrix).
"""
import unittest
from src.web_design_skills_matrix import AAASWebDesignSkillsMatrix

class TestAAASSkillsMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = AAASWebDesignSkillsMatrix()

    def test_minimum_150_skills_requirement(self):
        report = self.matrix.verify_all_150_skills_active()
        self.assertGreaterEqual(report["totalSkillsVerified"], 150, f"Znaleziono tylko {report['totalSkillsVerified']} umiejętności!")
        self.assertTrue(report["passedMinimum100Requirement"])
        self.assertTrue(report["passedAdvanced150Requirement"])
        self.assertEqual(report["certification"], "100% VERIFIED - 150 NEXT-GEN WEB DESIGN & AGENCY SKILLS ACTIVE")

    def test_specific_next_gen_skills(self):
        ota_cut = self.matrix.get_skill_by_id("103")
        self.assertIn("Price Parity", ota_cut["name"])

        higgs = self.matrix.get_skill_by_id("121")
        self.assertIn("Higgsfield CLI", higgs["name"])

        scale = self.matrix.get_skill_by_id("150")
        self.assertIn("Autonomous Scaling", scale["name"])

if __name__ == "__main__":
    unittest.main()
