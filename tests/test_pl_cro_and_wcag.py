"""
Testy dla agentów PL Conversion Architect (PL-CRO-2026) oraz WCAG / Core Web Vitals Auditor.
"""
import unittest
import os
import yaml

class TestPLConversionAndWCAGAgents(unittest.TestCase):
    def test_pl_conversion_architect_definition(self):
        path = "agents/pl_conversion_architect.yaml"
        self.assertTrue(os.path.exists(path), "Brak definicji YAML dla PL Conversion Architecta")
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self.assertEqual(data["name"], "PL Conversion Architect & Direct Booking Strategist Agent (PL-CRO-2026)")
            self.assertIn("emilkowalski/vaul", data["github_tools"])
            self.assertIn("BLIK", data["system_prompt"])
            self.assertGreaterEqual(len(data["tasks"]), 3)

    def test_wcag_core_vitals_auditor_definition(self):
        path = "agents/wcag_core_vitals_auditor.yaml"
        self.assertTrue(os.path.exists(path), "Brak definicji YAML dla WCAG / Core Vitals Auditora")
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self.assertEqual(data["name"], "WCAG 2.2 & Core Web Vitals Performance Auditor Agent")
            self.assertIn("WCAG 2.2", data["system_prompt"])
            self.assertIn("CLS", data["system_prompt"])

if __name__ == "__main__":
    unittest.main()
