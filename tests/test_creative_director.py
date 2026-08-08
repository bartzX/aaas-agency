"""
Testy dla agenta Dyrektora Kreatywnego (Creative Director / Art Director CD-AI).
"""
import unittest
import os
import yaml

class TestCreativeDirectorAgent(unittest.TestCase):
    def test_creative_director_definition(self):
        path = "agents/creative_director.yaml"
        self.assertTrue(os.path.exists(path), "Brak definicji YAML dla Dyrektora Kreatywnego")
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            self.assertEqual(data["name"], "Creative Director & Luxury Art Director Agent (CD-AI)")
            self.assertEqual(data["department"], "Creative & Executive Direction")
            self.assertIn("higgsfield-ai/cli", data["github_tools"])
            self.assertIn("Zero \"AI Slop\"", data["system_prompt"])
            self.assertGreaterEqual(len(data["kpis"]), 2)

if __name__ == "__main__":
    unittest.main()
